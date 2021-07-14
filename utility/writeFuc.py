



# 將 lists 寫入目標路徑中 
def writeFile(lists, writeFilePath):
    f = open(writeFilePath, "w")
    f.writelines(lists)
    f.close()