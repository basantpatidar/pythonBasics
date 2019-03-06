age = 26
print("My age is "+str(age)+" years")
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31,"January","March","May","July","August","October","December"))

print("""Number of days in months are like \n January:{2}
Fabruary:{0}
March:{2}
April:{1}
May:{2}
June:{1}
July:{2}
August:{2}
September:{1}
October:{2}
November:{1}
December:{2}""".format(28,30,31))

for i in range(1,12):
    print("No. {0} squred is {1:5} and cubed is {2:5}".format(i, i**2, i**3))

for i in range(1,12):
    print("No. {:2} squred is {:<5} and cubed is {:5}".format(i, i**2, i**3))

print("Pi is aproximately {0:12.10f}".format(22/7))