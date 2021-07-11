from os import listdir
from os.path import isfile, isdir, join

# 指定要列出所有檔案的目錄
mypath = "D:\dataClean\data"

# 取得所有檔案與子目錄名稱
files = listdir(mypath)

for file in files:
  # 產生檔案的絕對路徑
    fullpath = join(mypath, file)
  # 判斷 fullpath 是檔案還是目錄
    if isdir(fullpath):
        print("it's folder, there is something wrong!")
        continue
    f = open(fullpath, "r")
    fList = f.readlines()
    print(fullpath, " fList: ", fList)
    f.close()
