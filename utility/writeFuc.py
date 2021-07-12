



# 將 lists 寫入目標路徑中 
def writeFile(lists, writeFilePath):
    print("utilty util writeFile writeFile: ", writeFilePath)
    f = open(writeFilePath, "w")
    print("writeFile lists: ", lists)
    f.writelines(lists)
    f.close()