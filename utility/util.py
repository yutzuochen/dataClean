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


def writeFile(lis):
    f = open("D:\dataClean\clean\\filename.txt", "a")
    f.writelines(lis)
    f.close()
    print("finish write")