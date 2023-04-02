#Activity 1

# no1 = int(input("Enter vaue 1 "))
# no2 = int(input("Enter vaue 2 "))
# no3 = int(input("Enter vaue 3 "))
# minVal = min(no1,no2,no3)
# maxVal = max(no1,no2,no3)
# print("Minimum value is ",minVal)
# print("Maximum value is ",maxVal)

# if minVal < 20:
#     print("Less than 20")

##########################################################
#Activity 3

# import datetime

# birthYear = int(input("Enter your year of birth : "))
# age = datetime.date.today().year - birthYear
# if age > 18:
#     print("You're an adult")
# else:
#     print("You're a child")

##########################################################
#Activity 4

# i = 1
# sum = 0
# j = 0

# while i <= 10:
#     j = int(input("Enter a number :"))
#     sum = sum + j
#     j = 0
#     i = i +1

# print("Sum is ",sum)

##########################################################
#Activity 5

# def calcAvg(x,y,z):
#     sum = x + y + z
#     avg  = sum/3
#     return avg

# print(calcAvg(10,15,25))
# print(calcAvg(45,63,12)


#list
x = ["janith",125,52.25,"mango"]
print(x[0:5]) #print given range
print(x[0:5:2]) #print given range with sequence

#Dictionary
thisdict = {"id": 50, "name": "Janith", "salary": 100000.00}

print(thisdict)
print(type(thisdict))
print(thisdict["id"])
print(thisdict["name"])
print(thisdict["salary"])

thisdict["bonus"] = 25000.00

thisdict["address"] = {
    "no": 436,
    "lane": "galle road",
    "town": "gintota"
}

print(thisdict)
print()
#range
for no in range(10,20):
    print(no)

print()

for no in range(10,20,2):
    print(no)

print()

for no in range(0, 100, 20): 
   print(no)