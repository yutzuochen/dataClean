from typing import List


def getInfoVar(str):
    date = str[:8]      # Date
    code = str[8:12]    # Security Code
    act = str[14]       # Buy or Sell
    time = str[16:24]   # Trade Time
    price = str[37:44]  # Trade price
    vol = str[44:53]    # Trade share
    
    print("date: ", date)
    print("code: ", code)
    print("act: ", act)
    print("time: ", time)
    print("price: ", price)
    print("vol: ", vol)

def getCode(str):
    return str[8:12]

def getDate(str):
    return str[:8]

def getAct(str):
    return str[14]      # Buy or Sell
    
def getTime(str):
    return str[16:24]   # Trade Time
    
def getPrice(str):    
    return str[37:44]   # Trade price
    
def getVol(str):
    vol = str[44:53]    # Trade share


# 將 lists 寫入目標路徑中 
def writeFile(lists, writeFilePath):
    print("utilty util writeFile writeFile: ", writeFilePath)
    f = open(writeFilePath, "a")
    f.writelines(lists)
    f.close()


# def writeToFolder(lists, writeFilePath, targetFolder):
#     f = open(writeFilePath, "a")
#     f.writelines(lists)
#     f.close()
#     print("finish write")


# 用來拿到 list 中含有目標股票的交易
# targetStockCode  目標股票代碼的字串
# list             一個檔案中的交易清單
def getStock(targetStockCode, list):
    res = []
    for i in range(len(list)):
        aTra = list[i]
        codeInList = getCode(aTra)
        if codeInList != targetStockCode:
            continue
        # 去掉盤後交易
        if aTra[16:20] == "1430":
            continue
        res.append(aTra)
        
        
    return res