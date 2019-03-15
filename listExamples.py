# city = ["Big", "Better", "Best", "Bright"]
# city.append("Metro city")
#
# for state in city:
#     print("New York city is "+ state)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
# number = even + odd
# # number.sort()
# print(sorted(number))
# sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# if sorted_numbers == sorted(number):
#     print("Both lists are same")
# else:
#     print("No they are different lists")


# numbers = [even, odd]
#
# for number_set in numbers:
#     print(number_set)
#
#     for value in number_set:
#         print(value)

list_1 = []
list_2 = list()

print("list_1: {}".format(list_1))
print("List_2: {}".format(list_2))

if list_1 == list_2:
    print("The list are equal")

print(list("This makes string into list"))

anotherEven = sorted(even, reverse=True)
print(anotherEven)
print(anotherEven == even)

anotherEven.sort(reverse=True)
print(even)

sumEven = sum(even);
print(sumEven)