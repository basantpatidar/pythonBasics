class VirusDetector:
    def __init__(self,wid,version,authorizationCode,codeBuffer):
        self.__wid = wid,
        self.__version = version,
        self.__authorizationCode = authorizationCode,
        self.__codeBuffer = codeBuffer
        detectorCount = 0

    def getwid(self):
        return self.__wid
    def setwid(self, v):
        self.__wid = v

    def getversion(self):
        return self.__version
    def setversion(self, v):
        self.__version = v

    def getauthorizationCode(self):
        return self.__authorizationCode
    def setauthorizationCode(self, v):
        self.__authorizationCode = v

    def getcodeBuffer(self):
        return self.__codeBuffer
    def setcodeBuffer(self, v):
        self.__codeBuffer = v

    def countTrueBits(self,v):
        t = 0
        for i in v:
            i = int(i)
            if i == 1:
                t = t +1
        return t
    def countFalseBits(self, v):
        t = 0
        for i in v:
            i = int(i)
            if i == 0:
                t = t +1
        return t

    def countBytes(self,v):
        c = 0
        byte = 0
        for i in v:
            c += 1
            if c ==8:
                byte += 1
                c = 0
        return byte


    def checkBit(self,v):
        counter = 0
        v = str(v)
        length = len(v)
        for i in range (0, length):
            if (v[i] == '1'):
                return True
        return False

    def displayWidgetInfo(self):
        print("__________Virus Ditector :"+" "+ str(self.__wid)+" "+"_________________")
        print("Vesion: "+str(self.__version))
        print("Authorization Code: "+ str(self.__authorizationCode))
        print("Code Buffer Size "+ str(self.__codeBuffer))
        print("_____________________________________________________________")




cb = VirusDetector("12-1000-34","Lock-1","paceIS-612","5")
cb.countTrueBits("1111")
cb.countFalseBits("0000")
cb.countBytes("000")
print(cb.checkBit("0010"))
cb.displayWidgetInfo()


