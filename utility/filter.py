from readFolder import readFolderAndWrite

#DataFolder = "D:\stock_202003"
DataFolder = "D:\dataClean\data"
TarGetStock = "2330"
FolderWant2Write = "D:\dataClean\clean"

def filter(dataFolder, folderWant2Write, tarGetStock):
    # trans = getTSMC()
    # writeFile(trans) 
    readFolderAndWrite(dataFolder, folderWant2Write, tarGetStock)

filter(DataFolder, FolderWant2Write, TarGetStock)