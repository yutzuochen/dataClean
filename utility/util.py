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

# 09000064    
def getTime(str):
    return str[16:24]   # Trade Time
# 090000
def getTimeBySecond(str):
    return str[16:22]   # Trade Time

def getPrice_str(str):    
    return str[37:44]   # Trade price

def getPrice_float(str):    
    return float(str[37:44])   # Trade price

def getVol_str(str):
    return  str[44:53]    # Trade share

def getVol_int(str):
    return  int(str[44:53])

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


def lastFewMinute(abandonMinute):
    return int(133000) - int(abandonMinute)