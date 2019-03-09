#Write a program to ask users name and age and allow him/her if they are between 18-31 age group.
name = input("Enter your name: ")
age = int(input("{} please enter your age ".format(name)))
# if 18 <= age < 31:
if (age >= 18) and (age < 31):
    print("you are welcome")
else:
    print("I'm sorry. You are not elegible " + name)
