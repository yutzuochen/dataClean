def callDataFile():
    f = open("D:\dataClean\data\mth20200302test", "r")
    fArr = f.readlines()
    for i in range(len(fArr)):
        print(i," : ", fArr[i])
    f.close()


def callDataFile_test():
    f = open("D:\dataClean\data\\twoLine", "r")
    fArr = f.readlines()
    for i in range(len(fArr)):
        one = fArr[i]
        #print(i," : ", one)
        getInfoVar(one)
    f.close()