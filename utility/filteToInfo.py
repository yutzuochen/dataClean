from utility.util import getTimeBySecond 
from utility.util import getPrice
from utility.util import getVol

# 202003022330  B00900009800012357155580308.0000000400021590I7273
# return 提煉過的每秒資料 [[此秒,收盤價,最高價,最低價,成交量],[],...,[]]
def filteToInfo(list):
    if len(list) <= 0:
        print("utility/fileteToInfo fileteToInfo's list is empty")
        return 
    resList = []
    firstTra = list[0]
    preTime = getTimeBySecond(firstTra)
    highPrice, lowPrice = getPrice(firstTra), getPrice(firstTra)
    vol = 0
    for line in range(len(list)):
        aTra = list[line]
        thisTime = getTimeBySecond(aTra)
        if thisTime > preTime:
            # 設定上一刻時間的所有資料  [收盤價,最高價,最低價,成交量]
            info = thisTime + "," + price + "," + highPrice + ","+ lowPrice + "," + str(vol)
            resList.append(info)
        
        price = getPrice(aTra)
        highPrice = max(highPrice, price)
        lowPrice = min(lowPrice, price)
        vol += int(getVol(aTra))
        preTime = thisTime
    return resList

