from os import listdir
from os.path import isfile, isdir, join
from writeFuc import writeFile
from util import getStock

# 指定要列出所有檔案的目錄
#path = "D:\stock_202003"

def readFolderAndWrite(folderPath, folderWant2Write, targetStock):
  # 取得所有檔案與子目錄名稱
  files = listdir(folderPath)

  for file in files:
    # 產生檔案的絕對路徑
      fullpath = join(folderPath, file)
    # 判斷 fullpath 是檔案還是目錄
      if isdir(fullpath):
          print("it's folder, there is something wrong!")
          continue
      f = open(fullpath, "r")
      fList = f.readlines()
      stockList = getStock(targetStock, fList)
      # 將 filter 過的清單寫入目標 folder
      fileToWrite = folderWant2Write + "\\" + file + "_" + targetStock
      #print("readFolderAndWrite fileToWrite: ", fileToWrite)
      print(stockList)
      writeFile(stockList, fileToWrite)
      f.close()


