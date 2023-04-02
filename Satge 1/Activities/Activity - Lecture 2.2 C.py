import array

i = 1
j = 0
k = 0
valArr = array.array('i')

while i <= 5:
    j = int(input("Student {} mark :".format(i)))
    valArr.append(j)
    i = i +1

while k < len(valArr):
    mark = valArr[k]
    if mark > 75:
        print("Student {} grade : A".format(k+1))
    elif mark >= 65 and mark <= 75:
        print("Student {} grade : B".format(k+1))
    elif mark >= 55 and mark <= 64:
        print("Student {} grade : C".format(k+1))
    elif mark >= 45 and mark <= 54:
        print("Student {} grade : S".format(k+1))
    else:
        print("Student {} grade : F".format(k+1))

    k = k + 1
