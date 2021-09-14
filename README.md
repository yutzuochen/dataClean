# 想法

用鴻海訓練出來的演算法來預測台積電?

# Infomation


1. 在交易資料中，要決定放棄開盤前幾分鐘(E)和收盤前幾分鐘(O)的時間
1. 要決定從哪個時間開始計算資訊(abandonTime_open)以及
哪個時間開始放棄計算資訊(abandonTime_end)
2. 決定訊息區間的秒數(P)




# 個別的數據放在
dataClean/clean/2330/timeInfo

# 工具箱放在 utility 資料夾中








# 20210904 流程
(零) 從原始資料把特定股票資料萃取出來
將2317資    萃取特定股票 -> utility\extractTargetStock.py  
    把資訊從資料提出來，並做成 json 檔 -> getInfo_json.py

(一) 把30天的資料取出


(二) 針對每天的資料取出，並放到個別的資料夾，最好有一鍵就把所有技術指標整合在一起的功能。
        方法:全部資訊要整合到同一天的檔案內

    1. KD
    2. MACD
    3. MFI
    4. Bias
    5. 未來最高最低價 (另外要補百分比)

(二.5)
    (1)將(二)中做出的資料，同天的整合到一個文件中  
        使用 -> dataClean\techAllInOne.py     輸出檔案 -> dataClean\tech\2317\all

    (2)將上面做出來的數據整合到一分資料中 
        使用 -> dataClean\cleanData2ML.py     輸出檔案 -> dataClean\tech\2317\all\all.csv


(二) 把數據與資訊放到 google 上，跑出各天裡，每筆數據對應的理論未來最高價(最低)

(三) 設計買賣演算法

(四) 實驗數據中的報酬

