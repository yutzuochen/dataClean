from os import listdir
from os.path import isfile, isdir, join
import logging
from utility.filteToInfo import  filteToInfo_Json
from utility.writeFuc import writeFile
import datetime

TarGetStock = "2330"
DataFolder = "D:\dataClean\clean\\" + TarGetStock + "\data"
#FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\\timeInfo_json"
FolderToPut = "D:\dataClean\clean\\" + TarGetStock + "\\test"
#FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\\test\\timeInfo_json"

AbandonMinute = 20
logging.basicConfig(level=logging.DEBUG)

def main(dataFolderPath, tarGetStock, folderToPut):
    t1 = datetime.datetime.now()
    files = listdir(dataFolderPath)
    for file in files:
    # 產生檔案的絕對路徑
        fullpath = join(dataFolderPath, file)
    # 判斷 fullpath 是檔案還是目錄
        print("fullpath: ", fullpath)
        if isdir(fullpath):
            print("it's folder, there is something wrong!")
            continue
        f = open(fullpath, "r")
        fList = f.readlines()
        # 拿到該股票當日的每秒資訊
        infoList = filteToInfo_Json(fList, AbandonMinute)
        # 將 filter 過的清單寫入目標 folder
        fileToWrite = FolderToPut + "\\" + file + "_Info_" + tarGetStock
        #print("readFolderAndWrite fileToWrite: ", fileToWrite)
        writeFile(infoList, fileToWrite, folderToPut)
        f.close()
    t2 = datetime.datetime.now()
    print("t2: ", t2)
    logging.info(t2-t1)
    # 2021/07/14 18:00 實測花了 6.89 秒 

main(DataFolder, TarGetStock, FolderToPut)