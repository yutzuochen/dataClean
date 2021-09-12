import os
import logging


# 將 lists 寫入目標路徑中 
def writeFile(lists, writeFilePath, folderWant2Write):
    if not os.path.exists(folderWant2Write):
        os.makedirs(folderWant2Write)
        logging.debug("make direcotry: %s", folderWant2Write)
    f = open(writeFilePath, "w")
    logging.DEBUG("lists : %s", lists)
    f.writelines(lists)
    f.close()