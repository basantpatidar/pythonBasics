class ImperialDroid:
    def __init__(self, DroidID, DroidType, Head, UpperTorso, Arms, Legs):
        self.__DroidID = DroidID
        self.__DroidType = DroidType
        self.__Head = Head
        self.__UpperTorso = UpperTorso
        self.__Arms = Arms
        self.__Legs = Legs

    def displayInfo(self):
        print("Droid ID: ", self.__DroidID)
        print("Droid Type: ", self.__DroidType)

    def runDiagnostic(self):
        ID.displayInfo()

# Inheriting ImperialDroid
class SentryDroid_A(ImperialDroid):
    def __init__(self, DroidID, DroidType, Head, UpperTorso, Arms, Legs):
        super() .__init__(DroidID, "Alpha", Head, UpperTorso, Arms, Legs)

class SentryDroid_B(ImperialDroid):
    def __init__(self, DroidID, DroidType, Head, UpperTorso, Arms, Legs):
        super() .__init__(DroidID, "Beta", Head, UpperTorso, Arms, Legs)

class SentryDroid_C(ImperialDroid):
    def __init__(self, DroidID, DroidType, Head, UpperTorso, Arms, Legs):
        super() .__init__(DroidID, "Gamma", Head, UpperTorso, Arms, Legs)

class Arm:
    def __init__(self, IDNumber, AType):
        self.__IDNumber = IDNumber
        self.__AType = AType

    def displayInfo(self):
        print("Arms")
        print("ID Number: ", self.__IDNumber)
        print("Type Type: ", self.__AType)
		

#Inheriting Arm
class LeftArm(Arm):
    def __init__(self, IDNumber):
        super().__init__(IDNumber,"LeftARM")

#Inheriting Arm		
class RightArm(Arm):
    def __init__(self, IDNumber):
        super().__init__(IDNumber,"RightARM")


class Leg:
    def __init__(self, IDNumber, LType):
        self.__IDNumber = IDNumber
        self.__AType = LType

    def displayInfo(self):
        print("Legs")
        print("ID Number: ", self.__IDNumber)
        print("Type: ", self.__LType)

#Inheriting Leg		
class LeftLeg(Leg):
    def __init__(self, IDNumber):
        super().__init__(IDNumber,"Left Leg")

#Inheriting Leg
class RightLeg(Leg):
    def __init__(self, IDNumber):
        super().__init__(IDNumber,"Right Leg")


class Appendage:
    def __init__(self, IDNumber, CType):
        self.__IDNumber = IDNumber
        self.__CType = CType

    def displayInfo(self):
        print("Droid ID: ", self.__IDNumber)
        print("Droid Type: ", self.__CType)
class Cranial(Appendage):
    def __init__(self, IDNumber):
        super().__init__(IDNumber,"Cranial")

#Inheriting Appendage
class Torso(Appendage):
    def __init__(self, IDNumber):
        super().__init__(IDNumber,"Torso")



class DroidFactory:

    @staticmethod
    def buildDroid(ACount,BCount,CCount):
        droidList = []
        # Build a Droid
        i = 0
        while i < ACount:
            #Build A Arm
            LA = LeftArm('L-'+i); RA = RightArm('R-'+i); TA = (LA,RA)
            #Build a Leg
            LA = LeftLeg('L-'+i); RA = RightLeg('R-'+i); TA = (LL,RL)
            #Build Torso
            T = Torso('T'+i)
            #Build Head
            H = Cranial('C-'+i)
            # Assemble Droid
            A = SentryDroid_A('A-00' + i, H, T, TA, LA)
            droidList.append(A)


