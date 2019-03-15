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



