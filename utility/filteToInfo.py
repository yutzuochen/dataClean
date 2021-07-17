import json
import logging
from utility.util import getTimeBySecond
from utility.util import getPrice_str
from utility.util import getPrice_float
from utility.util import getVol_str
from utility.util import getVol_int
from utility.util import lastFewMinute
from utility.util import getNextTimeZone

#logging.basicConfig(level=logging.INFO)
# 202003022330  B00900009800012357155580308.0000000400021590I7273
# return 提煉過的每秒資料 [[此秒,收盤價,最高價,最低價,成交量],[],...,[]]
def filteToInfo(list, abandonMinute):
    if len(list) <= 0:
        logging.warn("utility/fileteToInfo fileteToInfo's list is empty")
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



def filteToInfo_Json(transListInADay, abandonTime_open, abandonTime_end, period) -> list:
    """[]

    Args:
        transListInADay (list): [a list contains every transaction for specific stock in a day]
        abandonTime_open (int): [the time we want to abandom before starting trading time]
        abandonTime_end (int): [the time we want to abandom after end trading time]
        peroid (int): [the intervetion we want to get infomation]

    Returns:
        [list]: [return the list of infomation we want to know]
    """
    if len(transListInADay) <= 0:
        print("utility/fileteToInfo fileteToInfo's list is empty")
        return 
    jsonList = []
    firstTra = transListInADay[0] # yu:應該要改掉? 
    price_now = getPrice_float(firstTra) # 上一層待改?
    highPrice = price_now
    lowPrice = price_now
    vol = 0
    #time_pre = getTimeBySecond(transListInADay[0])

    #nextTimeZone_start, nextTimeZone_end = getNextTimeZone(abandonTime_open, period)
    #nextTimeZone = getNextTimeZone(abandonTime_open, period)
    # if nextTimeZone == None:
    #     return
    nextTimeZone = abandonTime_open
    timeZone_pre = nextTimeZone
    for line in range(len(transListInADay)):
        aTra = transListInADay[line]
        if aTra == "\n":
            continue
        now = getTimeBySecond(aTra)
        # 放棄前幾秒 and 放棄後幾秒
        # abandonTime_open: 090220
        if now < abandonTime_open or now > abandonTime_end:
            continue
        # 檢查是否進入下個時區
        ## if yes
        #if now >= nextTimeZone:
        while now >= nextTimeZone:
            ### 1.開始結算，把資訊加入最終清單 2.變數歸零 3.設定下個時間區
            info_json = json.dumps(
                {
                    "time":timeZone_pre,
                    "closingPrice":price_now,
                    "highPrice":highPrice,
                    "lowPrice":lowPrice,
                    "vol":vol,
                }
            )
            jsonList.append(info_json +  "\n")
            vol = 0
            highPrice, lowPrice = price_now, price_now
            #nextTimeZone = getNextTimeZone(now, period)# yu:這裡有問題
            timeZone_pre = nextTimeZone
            nextTimeZone = getNextTimeZone(nextTimeZone, period)# yu:這裡有問題
            #time_pre = nextTimeZone


        # 開始計算
        price_now = getPrice_float(aTra)
        ## 看現價是否超過最高價或最低價
        highPrice = max(highPrice, price_now)
        lowPrice = min(lowPrice, price_now)
        ## 加上這次的交易量
        vol += getVol_int(aTra)
        time_pre = now
    return jsonList
