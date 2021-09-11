# """
# 將目標股票資訊從原始資料中掏出來
# """

# from util import getCode

# def getStock(targetStockCode):
#     f = open("D:\dataClean\data\\tsmcData", "r")
#     fList = f.readlines()
#     res = []
#     for i in range(len(fList)):
#         aTra = fList[i]
#         code = getCode(aTra)
#         if code != targetStockCode:
#             continue
#         res.append(aTra)
#     f.close()
#     return res

# getStock("2317")