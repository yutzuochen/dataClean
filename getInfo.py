from os import listdir
from os.path import isfile, isdir, join
from utility.filteToInfo import AbandonMinute, filteToInfo
from utility.writeFuc import writeFile
import datetime
import logging

TarGetStock = "2330"
DataFolder = "D:\dataClean\clean\\" + TarGetStock + "\data"
#FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\\timeInfo"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\\timeInfo" 
AbandonMinute = 5

def main(dataFolderPath, folderWant2Write, tarGetStock):
    t1 = datetime.datetime.now()
    files = listdir(dataFolderPath)
    for file in files:
    # 產生檔案的絕對路徑
        fullpath = join(dataFolderPath, file)
    # 判斷 fullpath 是檔案還是目錄
        logging.info("fullpath: %s", fullpath)
        if isdir(fullpath):
            logging.info("it's folder, there is something wrong!")
            continue
        f = open(fullpath, "r")
        fList = f.readlines()
        # 拿到該股票當日的每秒資訊
        infoList = filteToInfo(fList, AbandonMinute)
        # 將 filter 過的清單寫入目標 folder
        fileToWrite = folderWant2Write + "\\" + file + "_Info_" + tarGetStock
        #print("readFolderAndWrite fileToWrite: ", fileToWrite)
        writeFile(infoList, fileToWrite)
        f.close()
    t2 = datetime.datetime.now()
    print("t1: ", t1)
    print("t2: ", t2)
    logging.info("total cost time: ", t2-t1)

main(DataFolder, FolderWant2Write, TarGetStock)