from readFolder import readFolderAndWrite

#DataFolder = "D:\stock_202003"
DataFolder = "D:\stock_202003"
TarGetStock = "2330"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock

def filterAStock(dataFolder, folderWant2Write, tarGetStock):
    # trans = getTSMC()
    # writeFile(trans) 
    readFolderAndWrite(dataFolder, folderWant2Write, tarGetStock)


filterAStock(DataFolder, FolderWant2Write, TarGetStock)
