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
@sequence(DataFolder, FolderWant2Write)
def makeMFI(lis, abandonTime_start, s, q, m):
    # 拿到該股票當日每個時段間的資訊
    if not lis:
        logging.warn("the list is empty!!!")
        return
    resList = []
    
    # 確保每一行格式正確
    length = len(lis[0])

    preList_q = []
    EMA_s_pre = 0
    EMA_q_pre = 0
    DIFaccu = 0
    MACD_pre = 0
    for line in range(len(lis)):
        # 資料檢查
        periodData = lis[line]
        # if len(periodData) != length:
        #     logging.error("data format in this list is wrong, aTra: ", periodData)
        #     return
        # 載入該交易資料
        periodData_json = json.loads(periodData)
        closingPrice, vol = periodData_json["closingPrice"], periodData_json["vol"]
        highPrice, lowPrice =  periodData_json["highPrice"], periodData_json["lowPrice"]
        

        # 開始計算 MACD 使用到的參數
        DI = (closingPrice * 2 + closingPrice + highPrice)/4
        if line < q-1:
            preList_q.append(DI)
        elif line == q-1:
            EMA_s_cur = sum(preList_q)/q
            preList_q.append(DI)
            #MACD_pre =
        elif line < s-1:
            EMA_s_cur = EMA_s_pre * (s-1) / (s+1) +(DI*2/s+1)
            preList_q.append(DI)
            
        elif line == s-1:
            EMA_s_cur = EMA_s_pre * (s-1) / (s+1) +(DI*2/s+1)
            EMA_q_cur = sum(preList_q)/s
            DIFaccu += EMA_q_cur - EMA_s_cur
        elif line < s + m-2:
            EMA_s_cur = EMA_s_pre * (s-1) / (s+1) +(DI*2/s+1)
            EMA_q_cur = EMA_q_pre * (q-1) / (q+1) +(DI*2/q+1)
            DIFaccu += EMA_q_cur - EMA_s_cur
        elif line == s+m-2:
            EMA_s_cur = EMA_s_pre * (s-1) / (s+1) +(DI*2/s+1)
            EMA_q_cur = EMA_q_pre * (q-1) / (q+1) +(DI*2/q+1)
            # 首個 MACD: 9天內DIF總和 ÷ 9 
            MACD_pre = DIFaccu / m
        else:
            EMA_s_cur = EMA_s_pre * (s-1) / (s+1) +(DI*2/s+1)
            EMA_q_cur = EMA_q_pre * (q-1) / (q+1) +(DI*2/q+1)
            DIF = EMA_q_cur - EMA_s_cur
            
            MACD_cur = MACD_pre * (m-1) / (m+1) + DIF * 2/(m+1)
            OSC = DIF - MACD_cur
        
        
        resList = {"MACD":MACD_cur, "DIF":DIF, "OSC":OSC}
        EMA_s_pre = EMA_s_cur
        EMA_q_pre = EMA_q_cur
        MACD_pre = MACD_cur
    return resList



"""
MACD 說明
短線買賣點檢視柱線 OSC ，接近0時為短線買進或賣出訊號。
當柱線由負轉正時為買進訊號當柱線由正轉負時為賣出訊號。

"""









# makeMFI(DataFolder, FolderWant2Write, TarGetStock, nDay)


#sequnce(DataFolder, FolderWant2Write, TarGetStock, nDay)
