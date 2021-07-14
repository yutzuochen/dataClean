import json
import logging
from utility.util import getTimeBySecond
from utility.util import getPrice_str
from utility.util import getPrice_float
from utility.util import getVol_str
from utility.util import getVol_int
from utility.util import lastFewMinute

#logging.basicConfig(level=logging.INFO)
# 202003022330  B00900009800012357155580308.0000000400021590I7273
# return 提煉過的每秒資料 [[此秒,收盤價,最高價,最低價,成交量],[],...,[]]
def filteToInfo(list, abandonMinute):
    if len(list) <= 0:
        print("utility/fileteToInfo fileteToInfo's list is empty")
        return 
    resList = []
    firstTra = list[0]
    preTime = getTimeBySecond(firstTra)
    price = getPrice_str(firstTra)
    highPrice = price
    lowPrice = price
    vol = 0
    for line in range(len(list)):
        aTra = list[line]
        if aTra == "\n":
            continue

        now = getTimeBySecond(aTra)
        
        # 放棄最後幾分鐘的交易
        if int(now) > lastFewMinute(now, abandonMinute):
            break

        if int(now) > int(preTime):
            # 設定上一刻時間的所有資料  [收盤價,最高價,最低價,成交量]
            info = preTime + "," + price + "," + highPrice + ","+ lowPrice + "," + str(vol) + "\n"
            resList.append(info)
            # 資料重新歸零
            highPrice = getPrice_str(aTra)
            lowPrice = highPrice
            vol = 0
        
        price = getPrice_str(aTra)
        highPrice = max(highPrice, price)
        lowPrice = min(lowPrice, price)
        vol += int(getVol_str(aTra))
        preTime = now
        
    # 設定最後一刻的資料
    info = preTime + "," + price + "," + highPrice + ","+ lowPrice + "," + str(vol)
    resList.append(info)
    return resList


def filteToInfo_Json(list, abandonMinute):
    if len(list) <= 0:
        print("utility/fileteToInfo fileteToInfo's list is empty")
        return 
    jsonList = []
    firstTra = list[0]
    preTime = getTimeBySecond(firstTra)
    price = getPrice_float(firstTra) # 上一層待改?
    highPrice = price
    lowPrice = price
    vol = 0
    for line in range(len(list)):
        aTra = list[line]
        if aTra == "\n":
            continue
        now = getTimeBySecond(aTra)
        # 放棄最後幾分鐘的交易
        if int(now) > lastFewMinute(abandonMinute):
            #logging.debug("abandon time, now, lastFewMinute : %s %s", int(now), lastFewMinute(abandonMinute))
            break
        # 進入下個時段
        if int(now) > int(preTime):
            # 設定上一刻時間的所有資料  [收盤價,最高價,最低價,成交量]
            #info = preTime + "," + price + "," + highPrice + ","+ lowPrice + "," + str(vol) + "\n"
            info = {
                "time":preTime,
                "closingPrice":price,
                "highPrice":highPrice,
                "lowPrice":lowPrice,
                "vol":vol,
            }
            info_json = json.dumps(info)
            jsonList.append(info_json +  "\n")
            # 資料重新歸零
            price = getPrice_float(aTra)
            highPrice = price
            lowPrice = price
            vol = 0
        
        price = getPrice_float(aTra)              # string
        highPrice = max(highPrice, price)   # string
        lowPrice = min(lowPrice, price)     # string
        vol += getVol_int(aTra)          # int
        preTime = now
        
    # 設定最後一刻的資料
    info = {
                "time":preTime,
                "closingPrice":price,
                "highPrice":highPrice,
                "lowPrice":lowPrice,
                "vol":vol,
            }
    info_json = json.dumps(info)
    jsonList.append(info_json +  "\n")
    #logging.debug("now, info  2: %s , %s", now, info)
    #print("now, info  2: ", now, info)
    return jsonList