"""
1.先掃同天
2.依次掃過個技術指標
3.將時間變成 KEY，VALUE則為整合的內容
"""

from os import listdir
from constant import Foxconn
import csv
import json
import logging
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )

tarGetStock = Foxconn

DataFolder = "C:\\Users\mason\Desktop\dataClean\clean\\" + tarGetStock  + "\jsonInfo"
FolderWant2Write = "C:\\Users\mason\Desktop\dataClean\\tech\\" + tarGetStock + "\\all" 
techPath = "C:\\Users\mason\Desktop\dataClean\\tech\\" + tarGetStock + "\\"
techList = ["bias", "macd", "mfi", "kd"]

#kdPath = techPath + "\kd"
# 依次掃過 kd 檔案的每一天，並把每一刻的資訊與其他技術指標的同一時刻資料結合在一起

def allInOne(dataFolder, folderWant2Write, techPath, techList):
    filesList = listdir(dataFolder)
    hm = {}
    for day in filesList:
        dayList = []
        for tech in techList:
            path = techPath + tech + "\\" + day
            print("path: ", path)
            f = open(path, "r")
            fList = f.readlines()
            for l in fList:
                data_json = json.loads(l)
                # 合併
                if data_json["time"] in hm:
                    hm[data_json["time"]] = hm[data_json["time"]] | data_json
                else:
                    hm[data_json["time"]] = data_json
            f.close
        logging.debug("hm: %s", hm)
        csv_columns = ['time', 'KD','K','D', 'Bias', 'MACD', 'DIF', 'OSC', 'MFI']
        # print("folderWant2Write: ", folderWant2Write)
        # print("day: ", day)
        csv_file = folderWant2Write + "\\" + day + ".csv"

        # dictionary 轉 list
        for k in hm:
            dayList.append(hm[k])


        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in dayList:
                    writer.writerow(data)
        except IOError:
            print("I/O error")
        ### NOTE:輸出不會依時序，但不影響機器學習，以後有時間再修掉
        # 輸出成 LIST
        # for k, v in hm:
        #     file.append()


        

allInOne(DataFolder, FolderWant2Write, techPath, techList)




# csv_columns = ['KD','K','D', 'Bias', 'MACD', 'DIF', 'OSC', 'MFI']
# dict_data = [
# {'No': 1, 'Name': 'Alex', 'Country': 'India'},
# {'No': 2, 'Name': 'Ben', 'Country': 'USA'},
# {'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
# {'No': 4, 'Name': 'Smith', 'Country': 'USA'},
# {'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
# ]
# csv_file = "Names.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for data in dict_data:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")