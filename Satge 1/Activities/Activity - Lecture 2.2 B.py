import array

i = 1
j = 0
k = 0
sum = 0
valArr = array.array('i')

while i <= 10:
    j = int(input("Student {} mark :".format(i)))
    sum = sum + j
    valArr.append(j)
    i = i +1

maxVal = valArr[0]
minVal = valArr[0]

while k <= 8:
    if valArr[k+1] >= maxVal:
        maxVal = valArr[k+1]

    if valArr[k+1] <= minVal:
        minVal = valArr[k+1]    
    
    k = k + 1

print(valArr)
print("Max value is ",maxVal)
print("Min value is ",minVal)
print("Average is ",sum/10)