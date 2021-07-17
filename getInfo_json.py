from os import listdir
from os.path import isfile, isdir, join
import logging
from utility.filteToInfo import  filteToInfo_Json
from utility.writeFuc import writeFile
import datetime
logging.basicConfig(level=logging.DEBUG)


TarGetStock = "2330"
DataFolder = "D:\dataClean\clean\\" + TarGetStock + "\data"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\\test"
# m_s    e.g. 520 : 5分鐘20秒   
AbandonTime = 100
Period = 10
#FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\\timeInfo_json"
#FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\\test\\timeInfo_json"



def main(dataFolderPath, folderWant2Write, tarGetStock, abandonTime, period):
    t1 = datetime.datetime.now()
    files = listdir(dataFolderPath)
    for file in files:
    # 產生檔案的絕對路徑
        fullpath = join(dataFolderPath, file)
    # 判斷 fullpath 是檔案還是目錄
        logging.info("fullpath: %s", fullpath)
        if isdir(fullpath):
            logging.info("it's folder, there is something wrong! path:%s: ", fullpath)
            continue
        f = open(fullpath, "r")
        fList = f.readlines()
        # 拿到該股票當日的每秒資訊
        infoList = filteToInfo_Json(fList, abandonTime, period)
        # 將 filter 過的清單寫入目標 folder
        fileToWrite = folderWant2Write + "\\" + file + "_Info_" + tarGetStock
        writeFile(infoList, fileToWrite, folderWant2Write)
        f.close()
    t2 = datetime.datetime.now()
    logging.info("t2: %s", t2)
    logging.info(t2-t1)
    # 2021/07/14 18:00 實測花了 6.89 秒 

main(DataFolder, FolderWant2Write, TarGetStock, AbandonTime, Period)