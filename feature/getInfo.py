# from os import listdir
# from os.path import isfile, isdir, join
# from ..utility.filteToInfo import filteToInfo
# from ..utility.writeFuc import writeFile


# TarGetStock = "2330"
# DataFolder = "D:\dataClean\clean\\" + TarGetStock + "\data"
# FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\\timeIndo" 

# def main(dataFolderPath, folderWant2Write, tarGetStock):
#     files = listdir(dataFolderPath)
#     for file in files:
#     # 產生檔案的絕對路徑
#         fullpath = join(dataFolderPath, file)
#     # 判斷 fullpath 是檔案還是目錄
#         if isdir(fullpath):
#             print("it's folder, there is something wrong!")
#             continue
#         f = open(fullpath, "r")
#         fList = f.readlines()
#         # 拿到該股票當日的每秒資訊
#         infoList = filteToInfo(fList)
#         # 將 filter 過的清單寫入目標 folder
#         fileToWrite = folderWant2Write + "\\" + file + "_Info_" + tarGetStock
#         #print("readFolderAndWrite fileToWrite: ", fileToWrite)
#         writeFile(infoList, fileToWrite)
#         f.close()

# main(DataFolder, FolderWant2Write, TarGetStock)
# #filterAStock(DataFolder, FolderWant2Write, TarGetStock)
