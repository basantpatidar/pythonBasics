Language = ["Java","Python","R","Ruby","C#","Dot Net"]
for codingLag in Language:
    if codingLag == 'Ruby':
        continue
    print("Names of Languages is "+ codingLag)

Language = ["Java","Python","R","Ruby","C#","Dot Net"]
for codingLag in Language:
    if codingLag == 'Ruby':
        break
    print("Names of Languages is "+ codingLag)

car = ["tire","camera","steering","tail lamp","roof","seat","door"]
optional_in_car = ''
for items in car:
    if items == 'roof':
        optional_in_car = items
        break
else:
    print("I like sun roof in car")
if optional_in_car == "roof":
    print("It does'nt matter to me") 
