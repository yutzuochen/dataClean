TarGetStock = "2330"
### getHighLowPriceInNmin 

DataFolderPath = "D:\dataClean\clean\\" + TarGetStock  + "\\test"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\highLow" 
nPeriod = 14  # json data 的間隔

### getInfo_json

DataFolder = "/home/mason_chen/Documents/python/dataClean/clean/" + TarGetStock + "/data"
FolderWant2Write = "/home/mason_chen/Documents/python/dataClean/clean/" + TarGetStock + "/jsonInfo"
Period = 10 # 秒

### makebias

DataFolder = "D:\dataClean\clean\\" + TarGetStock  + "\\test"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\\bias" 


### makeKD

DataFolder = "D:\dataClean\clean\\" + TarGetStock  + "\\test"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\kd" 
nPeriod = 9

### makeMACD

TarGetStock = "2330"
DataFolder = "D:\dataClean\clean\\" + TarGetStock  + "\\test"
#DataFolder = "D:\dataClean\clean\\" + TarGetStock + "\\timInfo"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\macd"
qPeriod = 12
sPeriod = 26
xPeriod = 9

### makeMFI

DataFolder = "D:\dataClean\clean\\" + TarGetStock  + "\\test"
FolderWant2Write = "D:\dataClean\clean\\" + TarGetStock + "\mfi" 
n = 14

