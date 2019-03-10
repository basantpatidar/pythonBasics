for i in range (1,10):
    print("i is {} ".format(i))

number = "1,233,125,221,115,145,123"
for i in range(0,len(number)):
    print(number[i])

number = "1,233,125,221,115,145,123"
for i in range(0,len(number)):
    if number[i] in "0123456789":
        print(number[i],end='')


number = "1,233,125,221,115,145,123"
cleanedNumber = ''
for i in range(0,len(number)):
    if number[i] in "0123456789":
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

for num in number:
    if num in '0123456789':
        cleanedNumber = cleanedNumber + num

newNum = int(cleanedNumber)
print("Number is {} ".format(newNum))


for city in ["great","awesome","24x7","bright"]:
    print("New York city is "+ city)

for i in range(0,55,5):
        print("i is {}".format(i))

for i in range(1,11):
    j = i
    print("{:2} x 2 = {:2}".format(i, 2*j))

for i in range(1,11):
    for j in range(1,11):
        print("{} times {} is {}".format(i,j,i*j))
    print("--------*---------")

