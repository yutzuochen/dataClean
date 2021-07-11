from utility.tsmc import getTSMC
from utility.util import getInfoVar


def main():
    #oneLine("202003020050  S00900011800016830N52270087.5000000100011253I2826")
    #callDataFile_test()
    getInfoVar("202003020050  S00900011800016830N52270087.5000000100011253I2826")
    getTSMC()

main()