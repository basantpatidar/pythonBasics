print("Task 0")
def createNumberListFromFile(FP):

    data = []
    with open(FP,"r") as f:
        for i in f:
            n = i.split()
        for j in n:
            a = float(j)
            data.append(a)
    return data

# print(createNumberListFromFile("data.txt"))

#Finding largest number from file
def maxList(FP):
    data = createNumberListFromFile(FP)
    l = 0
    for i in data:
        if i > l:
            l = i
    return l

# print(maxList("data.txt"))


def writeFile(name):
    with open("name.txt",'w') as f:
        f.write(str(name)+ ' ')
        print(name)

writeFile("Basant")

def frequencyList(FP,L):
    data = []
    c = 0
    with open("data.txt","r") as f:
        for i in f:
            n = i.split()
        for j in n:
            a = float(j)
            data.append(a)
    for x in data:
        if x == L:
            c += 1
    print(c)
    with open(FP,'w') as f:
        f.write(str(c)+ ' ')

num = 43
frequencyList("freqList.txt",num)

def relativefreqList(FP,L):
    data = []
    c = 0
    with open("data.txt","r") as f:
        for i in f:
            n = i.split()
        for j in n:
            a = float(j)
            data.append(a)
    for x in data:
        if x == L:
            c += 1
    c = c/len(data)
    print(c)
    with open(FP,'w') as f:
        f.write(str(c)+ ' ')

num = 43
relativefreqList("Data1B.txt",num)

# Cumulatice relative frequency
def cumRelativefreqList(txt,L):
    data = []
    c = 0
    with open("FP.txt","r") as f:
        for i in f:
            n = i.split()
        for j in n:
            a = int(j)
            data.append(a)
    index = len(data)-1
    print(index)
    for x in data:
        if (x <= L & L <= index):
            c += 1
    c = (c)/len(data)
    print(c)
    with open(txt,'w') as f:
        f.write(str(c)+ ' ')

num = 7
cumRelativefreqList("Data1C.txt",num)

# Finding outlier
def outlierList(FP):
    data = []
    c = 0
    with open(FP,"r") as f:
        for i in f:
            n = i.split()
        for j in n:
            a = int(j)
            data.append(a)
    # Sorting to find median
    n = len(data)
    for i in range(n):
        for j in range(1,n):
            if data[j-1] > data[j]:
                (data[j-1], data[j]) = (data[j], data[j-1])
    print(data)
    # Finding Median
    dataLength = len(data)
    if (dataLength%2 == 0):
        median = (data[((dataLength)//2)]+data[((dataLength)//2)-1])//2
    else:
        median = data[(dataLength+1)//2]
    print("Median : ",median)
    # finding average of first quartile
    halflength = dataLength//2
    print("halfLen : ", halflength)
    if (halflength%2 == 0):
        firstQ = (data[((halflength)//2)]+data[((halflength)//2)-1])/2
    else:
        firstQ = data[(halflength+1)/2]
    print("FirstQ : ",firstQ)
    # finding Second Quartile
    lasthalf = round(int(dataLength*0.75))
    print("LastHalf : ",lasthalf)
    if (lasthalf%2 == 0):
        lastQ = (data[lasthalf]+data[lasthalf-1])/2
    else:
        lastQ = (data[lasthalf]+data[lasthalf-1])/2
    print("lastQ : ",lastQ)
    # finding interquartile range
    interquartile = lastQ - firstQ
    print("interquartile : ",interquartile)
    # finding inner fences
    interquartileI = interquartile * 1.5
    print("interquartileI : ",interquartileI)
    firstI = firstQ - interquartileI
    lastI = lastQ + interquartileI
    print("First and Last inner fences are : ",firstI," and ",lastI)
    # finding Outer fences
    interquartileO = interquartile * 3
    print("interquartileO : ",interquartileO)
    firstO = firstQ - interquartileO
    lastO = lastQ + interquartileO
    print("First and Last outer fences are : ",firstO," and ",lastO)
    outliers = []
    # writing the Outlier in file after opening file and finding the outliers
    with open("Data2A.txt",'w') as f:
        for innerOutlier in data:
            if (innerOutlier > lastI):
                print("Inner Outliers",innerOutlier)
                outliers.append(innerOutlier)
                f.write(str(innerOutlier)+ ' ')
        print(outliers)

outlierList("FP.txt")
