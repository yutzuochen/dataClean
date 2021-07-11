from util import getCode

def getStock(targetStockCode):

    f = open("D:\dataClean\data\\tsmcData", "r")
    fList = f.readlines()
    res = []
    for i in range(len(fList)):
        aTra = fList[i]
        code = getCode(aTra)
        if code != targetStockCode:
            continue
        res.append(aTra)
    f.close()
    return res