from os import listdir
from os.path import isfile, isdir, join
import logging
from utility.filteToInfo import filteToInfo
from utility.writeFuc import writeFile
import datetime
import json
from utility.util import sequence

logging.basicConfig(level=logging.INFO)
TarGetStock = "2330"
#DataFolder = "D:\dataClean\clean\\" + TarGetStock + "\\timInfo"
DataFolder = "D:\dataClean\clean\\" + TarGetStock  + "\\test"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\\bias" 



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

# 因之後的演算法中會預測 5 分鐘後的高低價，所以採 n = 5 * 6 = 30
@sequence(DataFolder = DataFolder, FolderWant2Write= FolderWant2Write, n = 30)
def makeBias(infoList, n):
    # 拿到該股票當日每個時段間的資訊
    if not infoList:
        logging.warn("the list is empty!!!")
        return
    resList = []


    closingPriceQueue = []
    for line in range(len(infoList)):
        # 資料檢查
        periodData = infoList[line]
        # if len(periodData) != length:
        #     logging.error("data format in this list is wrong, aTra: %s", periodData)
        #     return
        # 載入該交易資料
        periodData_json = json.loads(periodData)
        closingPrice = periodData_json["closingPrice"]
        #highPrice, lowPrice =  periodData_json["highPrice"], periodData_json["lowPrice"]
        
        # 開始計算 MFI 的參數
        closingPriceQueue.append(closingPrice)
        # n 日前不計算乖離率
        if len(closingPriceQueue) < n:
            continue
        elif len(closingPriceQueue) > n:
            closingPriceQueue.pop(0)
        else:
            pass
        
        nDayAveragePrice = sum(closingPriceQueue) / n
        Bias = (closingPrice - nDayAveragePrice) / nDayAveragePrice  * 100  
        
        # normal situation
        #Bias = (closingPrice - nDayAveragePrice) / nDayAveragePrice

        # append 的資料格式實例為 {"time":"090110", "Bias":95}
        resList.append({"time":periodData_json["time"], "Bias":Bias})
    #logging.warn("[makeBias] resList: %s", resList)
    return resList









# makeMFI(DataFolder, FolderWant2Write, TarGetStock, nDay)


#sequnce(DataFolder, FolderWant2Write, TarGetStock, nDay)
