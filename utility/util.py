import logging

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
def getTime(aTra):
    return aTra[16:24]   # Trade Time

def getTimeBySecond(aTra) -> str:
    """拿到這筆交易的時間，注意:微秒的時間會被捨棄，意味 02:00:25 會被視為 02:00:00

    Args:
        aTra (string): [單筆交易]

    Returns:
        [str]: [本秒的時間，e.g. 090000]
    """
    return aTra[16:22]   # Trade Time

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

def getNextTimeZone(timeZone_pre, period) -> str:
    nextTimeZone = str(int(timeZone_pre) + int(period))
    # 避免 "0900" 整數化時，首位數被拔掉
    if len(nextTimeZone) == len(timeZone_pre)+1:
        nextTimeZone = "0" + nextTimeZone
    # 現在時間的格式壞掉了
    if len(nextTimeZone) != len(timeZone_pre):
        logging.ERROR("[filteToInfo_Json] time unit was broken!")
        return None
    return nextTimeZone