import os
import logging


# 將 lists 寫入目標路徑中 
def writeFile(lists, writeFilePath, folderToPut):
    if not os.path.exists(folderToPut):
        os.makedirs(folderToPut)
        logging.debug("make direcotry: %s", folderToPut)
    f = open(writeFilePath, "w")
    f.writelines(lists)
    f.close()