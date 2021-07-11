from readFolder import readFolderAndWrite

#DataFolder = "D:\stock_202003"
DataFolder = "D:\stock_202003"
TarGetStock = "2330"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock

def filter(dataFolder, folderWant2Write, tarGetStock):
    # trans = getTSMC()
    # writeFile(trans) 
    readFolderAndWrite(dataFolder, folderWant2Write, tarGetStock)

filter(DataFolder, FolderWant2Write, TarGetStock)

# 2021/07/11 21:31 開始過濾