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