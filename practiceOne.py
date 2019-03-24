# Task 1 creating a list
fruitSales = [["Day", "Apples Sold", "Plums Sold", "Nectarines Sold", "Oranges Sold"],
              ["Monday", 100, 130, 200, 160],
              ["Tuesday", 125, 105, 195, 85],
              ["Wednesday", 150, 170, 150, 50],
              ["Thursday", 110, 90, 100, 210],
              ["Friday", 80, 180, 280, 180]]

for i in fruitSales:
    for j in i:
        print(j, end=" ")
    print("")


# Task 2 creating a dictionary
SoldFruit = {"Monday":[100, 130, 200, 160],
             "Tuesday":[125, 105, 195, 85],
             "Wednesday":[150, 170, 150, 50],
             "Thursday":[110, 90, 100, 210],
             "Friday":[80, 180, 280, 180]}
print(SoldFruit)

# Task 3 total no. of fruit sell by days
l = len(fruitSales)
l1 = len(fruitSales[0])
total = 0
for a in range(1, l):
    for b in range(1, l1):
        print(fruitSales[a][b], end=" ")
        total += fruitSales[a][b]
    print(" ---> TOTAL : ",total)
    total = 0;

# Task 4 using while loop showing total no. of fruit sell by days
i = 1
j = 1
total = 0
while i < len(fruitSales):
    while j < len(fruitSales[i]):
        print(fruitSales[i][j], end=" ")
        total += fruitSales[i][j]
        j += 1
    i += 1
    j = 1
    print(" ---> TOTAL : ",total)
    total = 0

# Task 5 nested for and while loop
for i in range(1, len(fruitSales)-1):
    total = 0
    temp = ''
    j = 0
    while j <= len(fruitSales[0]):
        if j == 0:
            temp = fruitSales[j][i]
            j += 1
            continue
        total += fruitSales[j][i]
        j += 1
    print('TOTAL', temp, 'for the week is:', total, 'lbs')

# Task 6  creating table of content using loops
fruits = ["Apples", "Plums", "Nectarines", "Oranges"]
print("__________MONDAY FRUITS SALES_________")
for key, value in SoldFruit.items():
    if key == "Monday":
        total = 0
        for i in range (0,4):
            total += value[i]
        for i in range (0,4):
            ratio = round(((value [i] / total) * 100),2)
            print("{:<12} {:<5} {:<7}".format(fruits[i]+':', value[i], ratio))
print("______________________________________")



