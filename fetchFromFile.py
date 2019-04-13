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
