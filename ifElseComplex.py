age = int(input("please enter your age: "))
# if (age >= 16) and (age<=65):
if 15 < age < 66:
    print("Have a good day at work")

if (age < 15) or (age > 66):
    print("Enjoy")
else:
    print("Have a good day")

x = False
if(x):
    print("x is true")
x = "false"
if(x):
    print("x is true and its second condition")

x= input("Enter something ")
if(x):
    print("Your entered {0}".format(x))
else:
    print("Nothing Entered")

print(not False)
print(not True)

school = "Pace"
letter = input("Enter a letter ")
if letter in school:
    print("Yes, its there")
else:
    print("No, its not there")