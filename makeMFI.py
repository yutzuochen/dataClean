import logging
import json
from utility.util import sequence

logging.basicConfig(level=logging.DEBUG)

TarGetStock = "2330"
#DataFolder = "D:\dataClean\clean\\" + TarGetStock + "\\timInfo"
DataFolder = "D:\dataClean\clean\\" + TarGetStock  + "\\test"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\mfi" 
n = 14


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

@sequence(DataFolder = DataFolder, FolderWant2Write= FolderWant2Write, n = n)
def makeMFI(infoList, n) -> list:
    # 拿到該股票當日每個時段間的資訊
    if not infoList:
        logging.warn("the list is empty!!!")
        return
    resList = []
    


    TP_pre = 0
    mfQueue = []
    posMF = 0
    negMF = 0
    for line in range(len(infoList)):
        # 資料檢查
        periodData = infoList[line]
        # if len(periodData) != length:
        #     logging.error("data format in this list is wrong, aTra: %s", periodData)
        #     return
        # 載入該交易資料
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
