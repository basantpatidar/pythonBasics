# A class with name "Stock" and finding Minimum, Maximum, Average, Variance, Range and Sigma
# for Stocks of Intel and AMD corporation given data.

class Stock:
    StockCount = 0

    def __init__(self, underlyingAsset, symbol, prices, startPrice, endPrice):
        self.__underlyingAsset = underlyingAsset
        self.__symbol = symbol
        self.__prices = prices
        self.__startPrice = startPrice
        self.__endPrice = endPrice
        Stock.StockCount += 1

    def getUnderlyingAssets(self):
        return self.__underlyingAsset

    def setUnderlyingAssets(self, v):
        self.__underlyingAsset = v

    def getSymbol(self):
        return self.__symbol

    def setSymbol(self, v):
        self.__symbol = v

    def getPrice(self):
        return self.__Price

    def setPrice(self, v):
        self.__Price = v

    def getStartPrice(self):
        return self.__StartPrice

    def setStartPrice(self, v):
        self.__StartPrice = v

    def getEndPrice(self):
        return self.__EndPrice

    def setEndPrice(self, v):
        self.__EndPrice = v

    def displayPrices(self):
        for i in self.__prices:
            print(str(i) + '...', end=' ')
        print()
    def Sum(self):
        total = 0
        for i in self.__prices:
            total = total+i
        return total
    def Average(self):
        mu = S1.Sum() / len(self.__prices)
        return mu
    def Varience(self):
        data = self.__prices
        c = 0
        x = 0
        total = 0
        totalX = 0
        for i in data:
            total = total + i
            c += 1
        average = total/c
        # print("Total : ",total," C : ",c, " Average : " ,average)
        for j in data:
            # X is Xi - underscore X
            x = (j - average) ** 2
            totalX += x
        # print("X :" ,x," TotalX : ", totalX)
        return totalX/(c)

    #Calculating Sigma
    def Sigma(self):
    # calculating Mean
        data = self.__prices
        total = 0
        c = 0
        for i in data:
            total = i + total
            c += 1
        mean = total/c
        # print(mean)
        totalX = 0
        for j in data:
            # X is Xi - underscore X
            x = (j - mean) ** 2
            totalX += x
        # print("X :" ,x," TotalX : ", totalX)
        return (totalX/(c-1)) ** 0.5

    # Calculating Range by subtracting lower value from higher
    def Range(self):
        data = self.__prices
        l = 0
        k = 0
        for i in data:
            if i > l:
                l = i

        c = 1
        for j in data:
            if c < len(data):
                if j < data[c]:
                    c += 1
                    k = j
        diff = l-k
        return diff
    # Finding higher value
    def High(self):
        data = self.__prices
        l = 0
        for i in data:
            if i > l:
                l = i
        return l
    # Finding lower value
    def Low(self):
        data = self.__prices
        min = data[0]
        l = 0
        for i in data:
            if i < min:
                min = i

        return min
    @staticmethod
    # Creating a function which will call all the above function using S1 object instance
    def DisplayStockInfo():
        S1.displayPrices()
        print(S1.Sum())
        print(S1.Average())
        print(S1.Varience())
        print(S1.Sigma())
        print(S1.Range())
        print(S1.High())
        print(S1.Low())

    # creating static method which will compare both the companies share values and return the highest
    @staticmethod
    def CompareStockPerformance(S1,S2):
        intel = S1.Range()
        AMD = S2.Range()
        if intel > AMD:
            return S1.getSymbol()
        elif AMD > intel:
            return S2.getSymbol()
        else:
            print("Both are equal")

# P is share data for Intel while Q is share data for AMD
P = [43.05, 43.10, 44.05,44.25, 44.50, 46.25]
Q = [41.15, 41.10, 43.95,40.15, 40.50, 40.25]
S1 = Stock('Intel Corporation', 'INTL', P, P[0],P[-1])
S2 = Stock('Advanced Micro Devices', 'AMD', Q, Q[0], Q[-1])
S1.displayPrices()
print(S1.Sum())
print(S1.Average())
print(S1.Varience())
print(S1.Sigma())
print(S1.Range())
print(S1.High())
print(S1.Low())
Stock.CompareStockPerformance(S1,S2)




