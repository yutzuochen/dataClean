"""

"""

from os import listdir
from os.path import isfile, isdir, join
import logging
from utility.filteToInfo import  filteToInfo_Json
from utility.writeFuc import writeFile
from constant import Foxconn
import datetime

logging.basicConfig(level=logging.DEBUG)


TarGetStock = Foxconn

### windows ver
DataFolder = "C:\\Users\mason\Desktop\dataClean\clean\\" + TarGetStock + "\data"
FolderWant2Write = "C:\\Users\mason\Desktop\dataClean\clean\\" + TarGetStock + "\\jsonInfo"

### linux ver
# DataFolder = "/home/mason_chen/Documents/python/dataClean/clean/" + TarGetStock + "/data"
# FolderWant2Write = "/home/mason_chen/Documents/python/dataClean/clean/" + TarGetStock + "/jsonInfo"

# m_s    e.g. 520 : 5分鐘20秒   
AbandonTime_open = "090040"
AbandonTime_end = "132400"
Period = 10


def main(dataFolderPath, folderWant2Write, tarGetStock, abandonTime_open, abandonTime_end, period):
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
        infoList = filteToInfo_Json(fList, abandonTime_open, abandonTime_end, period)
        # 將 filter 過的清單寫入目標 folder
        ## Windows ver
        fileToWrite = folderWant2Write + "\\" + file + "_Info_" + tarGetStock
        ## Linus ver
        #fileToWrite = folderWant2Write + "/" + file + "_Info_" 
        
        logging.info("fileToWrite %s: ", fileToWrite)
        writeFile(infoList, fileToWrite, folderWant2Write)
        f.close()
    t2 = datetime.datetime.now()
    logging.info("t2: %s", t2)
    logging.info(t2-t1)
    # 2021/07/14 18:00 實測花了 6.89 秒 

main(DataFolder, FolderWant2Write, TarGetStock, AbandonTime_open, AbandonTime_end, Period)