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

print(createNumberListFromFile("data.txt"))

#Finding largest number from file
def maxList(FP):
    data = createNumberListFromFile(FP)
    l = 0
    for i in data:
        if i > l:
            l = i
    return l

print(maxList("data.txt"))