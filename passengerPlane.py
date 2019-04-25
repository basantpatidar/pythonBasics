class Passenger:
    def __init__(self, IDNumber, SeatINumber):
        self.__IDNumber = IDNumber
        self.__SeatINumber = SeatINumber

    def getIDNumber(self):
        return self.__IDNumber
    def setIDNumber(self, v):
        self.__IDNumber = v

    def getSeatINumber(self):
        return self.__SeatINumber
    def setSeatINumber(self, v):
        self.__SeatINumber = v


    def get(self):
        return self.__
    def set(self, v):
        self.__ = v

    def displayPassengerInfo(self):
        print("Passenger ID: ",self.__IDNumber)
        print("Passenger Seat:", self.__SeatINumber)



class TurboProp:
    def __init__(self, variant, modelNumber, aircraftTailNumber, crew, passengerCapacity, passengers, length, wingSpan, height, currentSpeed, currentAltitude, isLanded, isAirborne):
        self.__variant = variant
        self.__modelNumber = modelNumber
        self.__aircraftTailNumber = aircraftTailNumber
        self.__crew = crew
        self.__passengerCapacity = passengerCapacity
        self.__passengers = passengers
        self.__length = length
        self.__wingSpan = wingSpan
        self.__height = height
        self.__currentSpeed = currentSpeed
        self.__currentAltitude = currentAltitude
        self.__isLanded = isLanded
        self.__isAirborne = isAirborne

    def getvariant(self):
        return self.__variant
    def setvariant(self, v):
        self.__variant = v

    def getmodelNumber(self):
        return self.__modelNumber
    def setmodelNumber(self, v):
        self.__modelNumber = v

    def getaircraftTailNumber(self):
        return self.__aircraftTailNumber
    def setaircraftTailNumber(self, v):
        self.__aircraftTailNumber = v

    def getcrew(self):
        return self.__crew
    def setcrew(self, v):
        self.__crew = v

    def getpassengerCapacity(self):
        return self.__passengerCapacity
    def setpassengerCapacity(self, v):
        self.__passengerCapacity = v

    def getpassengers(self):
        return self.__passengers
    def setpassengers(self, v):
        self.__passengers = v

    def getlength(self):
        return self.__length
    def setlength(self, v):
        self.__length = v

    def getwingSpan(self):
        return self.__wingSpan
    def setwingSpan(self, v):
        self.__wingSpan= v

    def getheight(self):
        return self.__height
    def setheight(self, v):
        self.__height = v

    def getcurrentSpeed(self):
        return self.__currentSpeed
    def setcurrentSpeed(self, v):
        self.__currentSpeed = v

    def getcurrentAltitude(self):
        return self.__currentAltitude
    def setcurrentAltitude(self, v):
        self.__currentAltitude = v

    def getisLanded(self):
        return self.__isLanded
    def setisLanded(self, v):
        self.__isLanded = v

    def getisAirborne(self):
        return self.__isAirborne
    def setisAirborne(self, v):
        self.__isAirborne = v

    # Getting Variant, Model Number and Aircraft tail Number
    def displayACInfo(self):
        print("Variant: ",self.__variant)
        print("Model Number: ", self.__modelNumber)
        print("Aircraft Tail Number: ",self.__aircraftTailNumber)

    # Getting Current speed, current altitude and True if plane is in Air
    def displayACStatus(self):
        print("______________Aircraft Status For: " + str(self.__aircraftTailNumber)+ "________________")
        print("Speed: ", self.__currentSpeed)
        print("Altitude: ", self.__currentAltitude)
        print("In Flight", self.__isAirborne)
        print()

    # i is the objects in the passengers list
    def displayPassengerInfo(self):
        for i in passengers:
            i.displayPassengerInfo()
        print()

    #getting takeoff status
    def TakeOff(self):
        if self.__isAirborne:
            print("Aircraft is already airborne")
            print()
        else:
            TP.setcurrentSpeed(75)
            TP.setcurrentAltitude(200)
            TP.setisLanded(False)
            TP.setisAirborne(True)
            print(str(self.__aircraftTailNumber)+" has taken off")
            print()

    def Land(self):
        if self.__isAirborne == False:
            print("Aircraft is already Landed")
            print()
        else:
            TP.setcurrentSpeed(0)
            TP.setcurrentAltitude(0)
            TP.setisLanded(True)
            TP.setisAirborne(False)
            print(str(self.__aircraftTailNumber)+" is Landed")
            print()




PS1 = Passenger('P-01', '1A')
PS2 = Passenger('P-02', '1B')
PS3 = Passenger('P-03', '2A')
PS4 = Passenger('P-04', '1B')

passengers = [PS1, PS2, PS3, PS4]

TP = TurboProp('BeechCraft 200', 'BC-001', 'US-BC-01', 2, 10, passengers, 43.6, 57.6, 14.4, 130, 5000, False, True)
TP.displayACStatus()
TP.displayPassengerInfo()
TP.Land()
TP.displayACStatus()
TP.TakeOff()
TP.displayACStatus()




