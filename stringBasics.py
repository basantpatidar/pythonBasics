city = "New York"
print(city)
print(city[0] + " prints First letter")
print(city[5] + " prints Fifth letter")
print(city[-1] + " prints last letter")
print(city[0:5] + " prints 0 index to 5th index letters")
print(city[:5] + " prints 0 to 5th")
print(city[5:] + " prints 5th to last")
print(city[-5:-2] + " prints second last to last fifth")
print(city[0:5:2] + " prints from 0 to 4th index while in steps of 2")
print(city[0:9:3] + " prints from 0 to 9th index while in steps of 3")

number = "1.123.145.126.456.423.111"
print(number[1::4] + " prints 1st and next 4th Index")
digits = "1, 1, 1, 2, 2, 2, 3, 3, 3, 4"
print(digits[0::3] + " prints oth and the next 3rd Index")
string1 = "Basant"
string2 = "Patidar"
print(string1 + string2)
print("School " * 5 + " prints 5 times school")
print("Pace " *(5+4)  + " prints 9 times pace")
print("Pace" *5 + " 4"  + " prints 'Pace' 5 times and '4' at last")
today = "Monday"
print("day" in today + " prints true if found day in monday")
print("Sun" in today + " prints flase if sun not found in monday")
print("Mon" in today)


