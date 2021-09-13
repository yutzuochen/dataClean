import logging
import json
import datetime

from os.path import isdir, join
from os import listdir
#from writeFuc import writeFile
from utility.writeFuc import writeFile

def getInfoVar(str):
    date = str[:8]      # Date
    code = str[8:12]    # Security Code
    act = str[14]       # Buy or Sell
    time = str[16:24]   # Trade Time
    price = str[37:44]  # Trade price
    vol = str[44:53]    # Trade share
    
    print("date: ", date)
    print("code: ", code)
    print("act: ", act)
    print("time: ", time)
    print("price: ", price)
    print("vol: ", vol)

def getCode(str):
    return str[8:12]

def getDate(str):
    return str[:8]

def getAct(str):
    return str[14]      # Buy or Sell

# 09000064    
def getTime(aTra):
    return aTra[16:24]   # Trade Time

def getTimeBySecond(aTra) -> str:
    """拿到這筆交易的時間，注意:微秒的時間會被捨棄，意味 02:00:25 會被視為 02:00:00

    Args:
        aTra (string): [單筆交易]

    Returns:
        [str]: [本秒的時間，e.g. 090000]
    """
    return aTra[16:22]   # Trade Time

def getPrice_str(str):    
    return str[37:44]   # Trade price

def getPrice_float(str):    
    return float(str[37:44])   # Trade price

def getVol_str(str):
    return  str[44:53]    # Trade share

def getVol_int(str):
    return  int(str[44:53])

# 用來拿到 list 中含有目標股票的交易
# targetStockCode  目標股票代碼的字串
# list             一個檔案中的交易清單
def getStock(targetStockCode, list):
    logging.info("getStock")
    res = []
    for i in range(len(list)):
        aTra = list[i]
        codeInList = getCode(aTra)
        if codeInList != targetStockCode:
            continue
        # 去掉盤後交易
        if aTra[16:20] == "1430":
            continue
        res.append(aTra)
    return res


def lastFewMinute(abandonMinute):
    return int(133000) - int(abandonMinute)

def getTimeZoneLastSecond(timeZone_pre, period) -> str:
    nextTimeZone = str(int(timeZone_pre) + period)
    nextTimeZone = examTimeUnit(nextTimeZone)
    # 避免 "0900" 整數化時，首位數被拔掉
    if len(nextTimeZone) + 1 == len(timeZone_pre):
        nextTimeZone = "0" + nextTimeZone
    # 現在時間的格式壞掉了
    if len(nextTimeZone) != len(timeZone_pre):
        print("nextTimeZone, timeZone_pre: ", nextTimeZone, "  ", timeZone_pre)
        logging.ERROR("[filteToInfo_Json] time unit was broken! nextTimeZone:%s , timeZone_pre:%s", nextTimeZone, timeZone_pre)
        return None
    return nextTimeZone
def examTimeUnit(time) -> str:
    """檢查分與秒是否超過60，若有，則進位

    Args:
        time (str): e.g. 090270  90270 95970 96013

    Returns:
        str: e.g. 090310
    """
    if int(time[-2]) >= 6:
        # 可能把開頭的0洗掉
        time = str(int(time) + 100 - 60)
    #print("Time[-4]: ", time[-4])
    if int(time[-4]) >= 6:
        time = str(int(time) + 10000 - 6000)
    return time


#print(examTimeUnit("090270"))

def dumpToJsonList(lis) -> list:
    """將型態為 dict 的元素的 list 轉為型態為 json 格式(str)的 list

    Args:
        MFIlist (list): 

    Returns:
        list:
    """
    resList = []
    #print("lis: ", lis)
    for i in lis:
        #print("i: ", i)
        resList.append(json.dumps(i) + "\n")
    return resList


# def sequence(*args, **kwargs):
#     #print("kwargs: ", kwargs["DataFolder"])
#     dataFolderPath = kwargs["DataFolder"]
#     folderWant2Write = kwargs["FolderWant2Write"]
#     #n = kwargs["nPeriod"]
#     qPeriod = kwargs["qPeriod"]
#     sPeriod = kwargs["sPeriod"]
#     xPeriod = kwargs["xPeriod"]
#     def wrap(methodFunc):
#         t1 = datetime.datetime.now()
#         # read folder
#         filesList = listdir(dataFolderPath)
#         for file in filesList:
#             fullpath = join(dataFolderPath, file)
#             # 將 filter 過的清單寫入目標 folder
#             logging.debug("將要讀取的檔案: %s", fullpath)
#             fileToWrite = folderWant2Write + "\\" + file + "_bias_" # yu:這裡要更正
#             logging.debug("將要寫入的檔案: %s", fileToWrite)
#             if isdir(fullpath):
#                 logging.error("it's folder, there is something wrong!")
#                 continue
#             # 打開該股票某天的資訊檔案
#             f = open(fullpath, "r")
#             fList = f.readlines()
            
#             # Do something
#             #MFIlist = makeMFI(fList)
#             resList = methodFunc(fList, qPeriod, sPeriod, xPeriod)
#             #logging.warn("MFIlist: %s", resList)
#             MFIjsonList = dumpToJsonList(resList)
#             writeFile(MFIjsonList, fileToWrite, folderWant2Write)
#             # end
#             f.close()

#         # 打印結束時間
#         t2 = datetime.datetime.now()
#         logging.info("t1: %s", t1)
#         logging.info("t2: %s", t2)
#         logging.info("total cost time: %s", t2-t1)
#         return 
#     return wrap
