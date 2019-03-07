# # votes eligibility check
# name = input("Please enter your name ")
# age = int(input("Enter your age {} ".format(name)))
# if age >= 18:
#     print("You can vote")
# else:
#     print("Please come after {} years".format(18-age))

# Number Guessing program
num = int(input("Please enter a number between 1 and 10 : "))
if num != 5:
    if num > 5:
        print("Please enter lower number")
    else:
        print("Please enter higher number")

    num = int(input())
    if num == 5:
        print("You guessed correctly")
    else:
        print("oops! wrong choice")
else:
    print("You got the number in first attempt")
