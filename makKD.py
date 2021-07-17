from os import listdir
from os.path import isfile, isdir, join
import logging
from utility.filteToInfo import filteToInfo
from utility.writeFuc import writeFile
import datetime
import json

TarGetStock = "2330"
DataFolder = "D:\dataClean\clean\\" + TarGetStock + "\\timInfo"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\mfi" 


def sequence(dataFolderPath, folderWant2Write):
    def wrap(methodFunc):
        t1 = datetime.datetime.now()
        # read folder
        filesList = listdir(dataFolderPath)
        for file in filesList:
            fullpath = join(dataFolderPath, file)
            # 將 filter 過的清單寫入目標 folder
            logging.debug("將要讀取的檔案: ", fullpath)
            fileToWrite = folderWant2Write + "\\" + file + "_mfi_" # + tarGetStock
            logging.debug("將要寫入的檔案: ", fileToWrite)
            if isdir(fullpath):
                logging.error("it's folder, there is something wrong!")
                continue
            # 打開該股票某天的資訊檔案
            f = open(fullpath, "r")
            fList = f.readlines()

            
            # Do something
            #MFIlist = makeMFI(fList)
            MFIlist = methodFunc(fList)

            
            writeFile(MFIlist, fileToWrite)

            # end
            f.close()

        # 打印結束時間
        t2 = datetime.datetime.now()
        logging.info("t1: %s", t1)
        logging.info("t2: %s", t2)
        logging.info("total cost time: %s", t2-t1)


# 2021_07_16:寫完這演算法，還沒測過
# list like: 
"""
[
    {"time": "090015", "closingPrice": 325.0, "highPrice": 325.0, "lowPrice": 325.0, "vol": 79000}
    {"time": "090020", "closingPrice": 325.0, "highPrice": 325.0, "lowPrice": 325.0, "vol": 101000}
    {"time": "090025", "closingPrice": 325.5, "highPrice": 325.5, "lowPrice": 325.5, "vol": 47000}
    {"time": "090030", "closingPrice": 325.5, "highPrice": 325.5, "lowPrice": 325.5, "vol": 68000}
]
"""

@sequence(DataFolder, FolderWant2Write)
def makeKD(lis, abandonTime_start, n):
    # 拿到該股票當日每個時段間的資訊
    if not lis:
        logging.warn("the list is empty!!!")
        return
    resList = []
    
    # 確保每一行格式正確
    length = len(lis[0])
    # 第一筆設為中間值
    K_pre = 50
    D_pre = 50
    nDayHighPriceQueue = []
    nDayLowPriceQueue = []
    for line in range(len(lis)):
        # 資料檢查
        periodData = lis[line]
        if len(periodData) != length:
            logging.error("data format in this list is wrong, aTra: ", periodData)
            return
        # 載入該交易資料
        periodData_json = json.loads(periodData)
        closingPrice, vol = periodData_json["closingPrice"], periodData_json["vol"]
        highPrice, lowPrice =  periodData_json["highPrice"], periodData_json["lowPrice"]

        nDayHighPriceQueue.append(highPrice)
        nDayLowPriceQueue.append(lowPrice)    
        # 開始計算 KD 值參數
        if nDayHighPriceQueue < n:
            continue
        
        elif nDayHighPriceQueue > n:
            nDayHighPriceQueue.pop(0)
            nDayLowPriceQueue.pop(0)
        else:
            pass

        nDayHighPrice = max(nDayHighPrice)
        nDayLowPrice = min(nDayLowPrice)
         
        # Normal situation
        RSV = (closingPrice- nDayLowPrice) / (nDayHighPrice-nDayLowPrice) * 100
        K_cur = K_pre * (2/3) + RSV * (1/3)
        D_cur = D_pre * (2/3) + K_cur * (1/3)
        KD = K_cur - D_cur
        # append 的資料格式實例為 {"time":"090110", "KD":15}
        resList.append({"time":periodData_json["time"], "KD":KD, "K":K_cur, "D":D_cur})
        K_pre = K_cur
        D_pre = D_cur
    return resList # yu:這裡可能出錯，回頭來看的時候記得確認









# makeMFI(DataFolder, FolderWant2Write, TarGetStock, nDay)


#sequnce(DataFolder, FolderWant2Write, TarGetStock, nDay)
