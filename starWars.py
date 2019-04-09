class TieFighterPilot:
    def __init__(self,IDNumber, yearsOfservice, rank):
        self.__IDNumber = IDNumber
        self.__yearsOfservice = yearsOfservice
        self.__rank = rank


    def getIDNumber(self):
        return self.__IDNumber
    def setIDNumber(self, v):
        self.__IDNumber = v

    def getyearsOfservice(self):
        return self.__yearsOfservice
    def setyearsOfservice(self,v):
        self.__yearsOfservice = v

    def getrank(self):
        return self.__rank
    def setrank(self,v):
        self.__rank = v


    def displayInfo(self):
        print(self.__IDNumber+ " "+ self.__rank + " " + str(self.__yearsOfservice))


    def FliesTieFighter(self, v):
        pass





class TieFighter:
    def __init__(self,IDNumber, pilot, cannon, shield):
        self.__IDNumber = IDNumber
        self.__pilot = pilot
        self.__cannon = cannon
        self.__shield = shield


    def getIDNumber(self):
        return self.__IDNumber
    def setIDNumber(self, v):
        self.__IDNumber = v

    def getpilot(self):
        return self.__pilot

    def setpilot(self,v):
        self.__pilot = v

    def getcannon(self):
        return self.__cannon
    def setcannon(self,v):
        self.__cannon = v
    def getshield(self):
        return self.__shield

    def setshield(self):
        self.__shield

    def maneuver(self, v):
        print("I am firing my cannons")
        self.setAmmoCount(self.getAmmoCount()-2)
        print(self.AmmoCount)
    def firesCannons(self, v):
        pass
    def displayPilotInfo(self):
        self.__Pilot.displayInfo()

    @staticmethod
    def displayPilots(L):
        for i in L:
            i.displayPilotInfo()
            print()


TFP1 = TieFighterPilot("TP001",4, "LT")
TFP1 = TieFighterPilot("TP002",4, "CAPT")
TFP1 = TieFighterPilot("TP003",4, "LT")
TFP1 = TieFighterPilot("TP004",4, "CON")


TF1 = TieFighter("TF1", TFP1, 4, True)
TF2 = TieFighter("TF2", TFP1, 4, True)
TF3 = TieFighter("TF3", TFP1, 4, True)
TF4 = TieFighter("TF4", TFP1, 4, True)
L = [TF1, TF2, TF3, TF4]
TFP1.displayInfo()
TieFighter.displayPilots(L)

# calling Stating method
# creating static method
# private variable
#