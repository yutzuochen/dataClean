""" 
提取某筆資料的未來 N 分鐘內的最大漲幅與最大跌幅
"""
from os import listdir
from os.path import isfile, isdir, join
import logging
import json
from utility.writeFuc import writeFile
from utility.util import dumpToJsonList
from constant import Foxconn

logging.basicConfig(level=logging.DEBUG)

TarGetStock = Foxconn

DataFolderPath = "C:\\Users\mason\Desktop\dataClean\clean\\" + TarGetStock  + "\jsonInfo"
FolderWant2Write = "C:\\Users\mason\Desktop\dataClean\\tech\\" + TarGetStock + "\highLowPercent" 
nPeriod = 14


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


def getHighLowPrice(nPeriod, dataFolderPath, folderWant2Write, tarGetStock):
    ### 讀取指定資料夾
    files = listdir(dataFolderPath)

    # 讀取個別檔案
    for file in files:
    # 產生檔案的絕對路徑
        fullpath = join(dataFolderPath, file)
        resultList = []
    # 判斷 fullpath 是檔案還是目錄
        logging.info("fullpath: %s", fullpath)
        if isdir(fullpath):
            logging.info("it's folder, there is something wrong!")
            continue
        f = open(fullpath, "r")
        fList = f.readlines()
        hmList = []
        # 將 filter 過的清單寫入目標 folder
        for line in range(len(fList)):
            # 資料檢查
            periodData = fList[line]
            # 載入該交易資料
            periodData_json = json.loads(periodData)

            # 檢查後幾個間隔的最高最低價
            h, l = periodData_json["highPrice"],  periodData_json["lowPrice"]
            price_now = periodData_json["closingPrice"]
            for p in range(1, nPeriod+1):
                if line+p >= len(fList):
                    break
                next_json = json.loads(fList[line + p])
                h = max(h, next_json["highPrice"])
                l = min(l, next_json["lowPrice"])
                hPercent = (h - price_now) / price_now
                #lPercent = (price_now - l) / price_now

 
            #hmList.append(periodData_json)
            hmList.append({"time":periodData_json["time"],"highPrice":h, "increasePercent": hPercent})
        resultList = dumpToJsonList(hmList)
        ### 寫入檔案
        fileToWrite = folderWant2Write + "\\" + file 
        writeFile(resultList, fileToWrite, folderWant2Write)
  
        f.close()

        
    
getHighLowPrice(nPeriod, DataFolderPath, FolderWant2Write, TarGetStock)

    
