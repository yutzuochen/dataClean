from tsmc import getTSMC
from util import writeFile

def main():
    trans = getTSMC()
    writeFile(trans) 

print(main())