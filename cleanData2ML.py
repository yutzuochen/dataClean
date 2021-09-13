"""
要將缺失值和時間拿掉，已讓資料可以直接未給 ML

"""
from os import listdir
from os.path import isfile, isdir, join
import logging
from constant import Foxconn
from utility.writeFuc import writeFile

targetStock = Foxconn
DataFolder = "C:\\Users\mason\Desktop\dataClean\\tech\\" + targetStock  + "\\all"
FileWant2Write = "C:\\Users\mason\Desktop\dataClean\\tech\\" + targetStock + "\\all\\all.csv" 

def cleanData2ML(dataFolder, fileWant2Write):
    filesList = listdir(dataFolder)
    fw = open(FileWant2Write, "a")
    for file in filesList:
        fullpath = join(dataFolder, file)
        # 將 filter 過的清單寫入目標 folder
        logging.debug("將要讀取的檔案: %s", fullpath)
        #fileToWrite = folderWant2Write + "\\"  + file  # yu:這裡要更正
        logging.debug("將要寫入的檔案: %s", fileWant2Write)
        if isdir(fullpath):
            logging.error("it's folder, there is something wrong!")
            continue
        # 打開該股票某天的資訊檔案
        f = open(fullpath, "r")
        #fList = f.readlines()
        
        fw.write(f.read())

        f.close()
    fw.close()


cleanData2ML(DataFolder, FileWant2Write)