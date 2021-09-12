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
                next_json = json.loads(fList[line + p])
                h = max(h, next_json["highPrice"])
                l = min(l, next_json["lowPrice"])
                hPercent = (h - price_now) / price_now
                lPercent = (price_now - l) / price_now

            periodData_json["highPrice"] = h
            periodData_json["lowPrice"] = l
            periodData_json["increasePercent"] = hPercent
            periodData_json["decreasePercent"] = lPercent
            
            resultList.append(dumpToJsonList(periodData_json))
            ### 寫入檔案
            fileToWrite = folderWant2Write + "\\" + file + "_highlow_" + tarGetStock
            writeFile(resultList, fileToWrite, folderWant2Write)
  
        
        f.close()

        
    
getHighLowPrice(nPeriod, DataFolderPath, FolderWant2Write, TarGetStock)

    
"""
    for line in range(len(infoList)):
        # 資料檢查
        periodData = infoList[line]
        # if len(periodData) != length:
        #     logging.error("data format in this list is wrong, aTra: %s", periodData)
        #     return
        # 載入該交易資料
        #logging.debug("periodData: %s", periodData)
        periodData_json = json.loads(periodData)
        closingPrice, vol = periodData_json["closingPrice"], periodData_json["vol"]
        highPrice, lowPrice =  periodData_json["highPrice"], periodData_json["lowPrice"]
        
        # 開始計算 MFI 的參數
        TP_cur = (highPrice + lowPrice + closingPrice) / 3
        MoneyFlow = TP_cur * vol
        # 第一筆資料取得 TP_0 就跳過
        if line == 0:
            TP_pre = TP_cur
            continue
        
        else:
            if len(mfQueue) > n:
                logging.error("the data queue is encountering something wrong")
                return
            # 前幾筆資料還沒累積出 posMF and negMf
            if len(mfQueue) < n:
                if  TP_cur > TP_pre:
                    posMF += MoneyFlow # 過去n日的正金錢流(Positive Money Flow)
                    mfQueue.append(MoneyFlow)
                elif TP_cur < TP_pre:
                    negMF += MoneyFlow #過去n日的負金錢流(Negative Money Flow)
                    mfQueue.append(-MoneyFlow)
            else:
                # 拿掉最先進來的 MF， YU:使用 sliding windows 技巧，你說屌不屌
                if mfQueue[0] > 0: 
                    posMF -= mfQueue.pop(0)
                else:
                    negMF -= mfQueue.pop(0)
                if  TP_cur > TP_pre:
                    posMF += MoneyFlow
                    mfQueue.append(MoneyFlow)
                elif TP_cur < TP_pre:
                    mfQueue.append(-MoneyFlow)

            # 分母不能為 0
            if negMF == 0:
                MFI = 100
            else:
                MoneyRatio = posMF / negMF
                MFI = 100 - (100 / (1 + MoneyRatio))
            
            # append 的資料格式實例為 {"time":"090110", "MFI":95}
            resList.append({"time":periodData_json["time"], "MFI":MFI})
            TP_pre = TP_cur
    return resList # yu:這裡可能出錯，回頭來看的時候記得確認






#print(makeMFI())



# makeMFI(DataFolder, FolderWant2Write, TarGetStock, nDay)


# sequnce(DataFolder, FolderWant2Write, TarGetStock, nDay)

"""