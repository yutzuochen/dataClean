from readFolder import readFolderAndWrite
import logging

Foxconn = "2317"
TarGetStock = Foxconn
DataFolder = "C:\\Users\mason\Documents\stock202003"

FolderWant2Write = "C:\\Users\mason\Desktop\dataClean\clean\\" + TarGetStock

def filterAStock(dataFolder, folderWant2Write, tarGetStock):
    # trans = getTSMC()
    # writeFile(trans) 
    print("hihi")
    logging.warning("gogo")
    
    readFolderAndWrite(dataFolder, folderWant2Write, tarGetStock)


filterAStock(DataFolder, FolderWant2Write, TarGetStock)
