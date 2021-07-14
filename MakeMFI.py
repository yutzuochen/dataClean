from os import listdir
from os.path import isfile, isdir, join
import logging
from utility.filteToInfo import filteToInfo
from utility.writeFuc import writeFile
import datetime



TarGetStock = "2330"
DataFolder = "D:\dataClean\clean\\" + TarGetStock + "\\timInfo"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\mfi" 

def makeMFI(lis):
        # 拿到該股票當日的每秒資訊
        #fList = f.readlines()
    if not lis:
        logging.warn("the list is empty!!!")
        return
    length = len(lis[0])
    for line in range(len(lis)):
        aTra = lis[line]
        if len(aTra) != length:
            logging.error("data format in this list is wrong, aTra: ", aTra)
            return

        

        TypicalPrice_cur = (highPrice + lowPrice + ClosingPrice) / 3
        
        MoneyFlow = TypicalPrice * minuteVolume

        # 注意:若前一秒沒有交易，則
        if  TypicalPrice_cur > TypicalPrice_pre:
            posMF =  # 過去n日的正金錢流(Positive Money Flow)

        elif TypicalPrice_cur < TypicalPrice_pre:
            negMF =  #過去n日的負金錢流(Negative Money Flow)

        if negMF == 0:
            MFI = 100
        else:
            MoneyRatio = posMF / negMF
            MFI = 100 - (100 / (1 + MoneyRatio))



        infoList = filteToInfo(fList)
        #print("infoList: ", infoList)
        # 將 filter 過的清單寫入目標 folder
        fileToWrite = folderWant2Write + "\\" + file + "_Info_" + tarGetStock
        #print("readFolderAndWrite fileToWrite: ", fileToWrite)
        writeFile(infoList, fileToWrite)
        f.close()


def main(dataFolderPath, folderWant2Write, tarGetStock, nDay):
    t1 = datetime.datetime.now()
    # read folder
    
    filesList = listdir(dataFolderPath)
    for file in filesList:
        fullpath = join(dataFolderPath, file)
        # 將 filter 過的清單寫入目標 folder
        logging.debug("將要讀取的檔案: ", fullpath)
        fileToWrite = folderWant2Write + "\\" + file + "_mfi_" + tarGetStock
        logging.debug("將要寫入的檔案: ", fileToWrite)
        if isdir(fullpath):
            logging.error("it's folder, there is something wrong!")
            continue
        # 打開該股票某天的資訊檔案
        f = open(fullpath, "r")
        fList = f.readlines()


        # Do something
        MFIlist = makeMFI(fList)


        
        writeFile(MFIlist, fileToWrite)

        # end
        f.close()

    # 打印結束時間
    t2 = datetime.datetime.now()
    print("t1: ", t1)
    print("t2: ", t2)
    print("total cost time: ", t2-t1)








# makeMFI(DataFolder, FolderWant2Write, TarGetStock, nDay)


main(DataFolder, FolderWant2Write, TarGetStock, nDay)
