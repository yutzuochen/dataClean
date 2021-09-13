from os import listdir
from os.path import isdir, join
import logging
import json
from utility.util import dumpToJsonList
from constant import Foxconn
from utility.writeFuc import writeFile

logging.basicConfig(level=logging.DEBUG)


TarGetStock = Foxconn
DataFolder = "C:\\Users\mason\Desktop\dataClean\clean\\" + TarGetStock  + "\jsonInfo"
FolderWant2Write = "C:\\Users\mason\Desktop\dataClean\\tech\\" + TarGetStock + "\macd"

qPeriod = 12
sPeriod = 26
xPeriod = 9

"""
list like:
[ 
    {"time": "090015", "closingPrice": 325.0, "highPrice": 325.0, "lowPrice": 325.0, "vol": 79000}
    {"time": "090020", "closingPrice": 325.0, "highPrice": 325.0, "lowPrice": 325.0, "vol": 101000}
    {"time": "090025", "closingPrice": 325.5, "highPrice": 325.5, "lowPrice": 325.5, "vol": 47000}
    {"time": "090030", "closingPrice": 325.5, "highPrice": 325.5, "lowPrice": 325.5, "vol": 68000}
]
"""


# q:快線的時間，一般取12  s:慢線的時間，一般取26
def makeMACD(dataFolder, folderWant2Write, qPeriod, sPeriod, xPeriod):
    filesList = listdir(dataFolder)
    for file in filesList:
        fullpath = join(dataFolder, file)
        # 將 filter 過的清單寫入目標 folder
        logging.debug("將要讀取的檔案: %s", fullpath)
        fileToWrite = folderWant2Write + "\\" + file  # yu:這裡要更正
        logging.debug("將要寫入的檔案: %s", fileToWrite)
        if isdir(fullpath):
            logging.error("it's folder, there is something wrong!")
            continue
        # 打開該股票某天的資訊檔案
        f = open(fullpath, "r")
        fList = f.readlines()
        
        # Do something
        resList = calculateMACD(fList, sPeriod, qPeriod, xPeriod)
        #logging.warn("resList: %s", resList)
        macdJsonList = dumpToJsonList(resList)
        writeFile(macdJsonList, fileToWrite, folderWant2Write)
        # end
        f.close()

def calculateMACD(lis, sPeriod, qPeriod, xPeriod):
    # 拿到該股票當日每個時段間的資訊
    if not lis:
        logging.warn("the list is empty!!!")
        return
    resList = []
    preList_q = []
    EMA_s_pre = 0
    EMA_q_pre = 0
    DIFaccu = 0
    MACD_pre = 0
    MACD_cur = None
    EMA_s_cur = 0
    EMA_q_cur = 0
    for line in range(len(lis)):
        # 資料檢查
        periodData = lis[line]

        # 載入該交易資料
        periodData_json = json.loads(periodData)
        closingPrice = periodData_json["closingPrice"]
        highPrice, lowPrice =  periodData_json["highPrice"], periodData_json["lowPrice"]
        
        # 開始計算 MACD 使用到的參數
        DI = (closingPrice * 2 + lowPrice + highPrice)/4
        if line < qPeriod-1:
            preList_q.append(DI)
            
        elif line == qPeriod-1:
            EMA_s_cur = sum(preList_q)/qPeriod
            preList_q.append(DI)
        elif line < sPeriod-1:
            EMA_s_cur = EMA_s_pre * (sPeriod-1) / (sPeriod+1) +(DI*2/sPeriod+1)
            preList_q.append(DI)
            
        elif line == sPeriod-1:
            EMA_s_cur = EMA_s_pre * (sPeriod-1) / (sPeriod+1) +(DI*2/sPeriod+1)
            EMA_q_cur = sum(preList_q)/sPeriod
            DIFaccu += EMA_q_cur - EMA_s_cur
        elif line < sPeriod + xPeriod-2:
            EMA_s_cur = EMA_s_pre * (sPeriod-1) / (sPeriod+1) +(DI*2/sPeriod+1)
            EMA_q_cur = EMA_q_pre * (qPeriod-1) / (qPeriod+1) +(DI*2/qPeriod+1)
            DIFaccu += EMA_q_cur - EMA_s_cur
        elif line == sPeriod+xPeriod-2:
            EMA_s_cur = EMA_s_pre * (sPeriod-1) / (sPeriod+1) +(DI*2/sPeriod+1)
            EMA_q_cur = EMA_q_pre * (qPeriod-1) / (qPeriod+1) +(DI*2/qPeriod+1)
            # 首個 MACD: 9天內DIF總和 ÷ 9 
            MACD_pre = DIFaccu / xPeriod
        else:
            EMA_s_cur = EMA_s_pre * (sPeriod-1) / (sPeriod+1) +(DI*2/sPeriod+1)
            EMA_q_cur = EMA_q_pre * (qPeriod-1) / (qPeriod+1) +(DI*2/qPeriod+1)
            DIF = EMA_q_cur - EMA_s_cur
            
            MACD_cur = MACD_pre * (xPeriod-1) / (xPeriod+1) + DIF * 2/(xPeriod+1)
            OSC = DIF - MACD_cur
        
        if MACD_cur != None:
            #resList = {"MACD":MACD_cur, "DIF":DIF, "OSC":OSC}
            resList.append({"time":periodData_json["time"], "MACD":MACD_cur, "DIF":DIF, "OSC":OSC})
            MACD_pre = MACD_cur
        
        EMA_s_pre = EMA_s_cur
        EMA_q_pre = EMA_q_cur
        #MACD_pre = MACD_cur
    return resList



"""
MACD 說明
短線買賣點檢視柱線 OSC ，接近0時為短線買進或賣出訊號。
當柱線由負轉正時為買進訊號當柱線由正轉負時為賣出訊號。

"""


makeMACD(DataFolder, FolderWant2Write, qPeriod, sPeriod, xPeriod)







