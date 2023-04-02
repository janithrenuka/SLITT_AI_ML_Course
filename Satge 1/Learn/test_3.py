import numpy as np

def hello():
    print("Hello world!")

def calc(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    
    return sum,sub,mul,div

myarr1 = np.array([1,2,3,4,5,6,7,8,9,10]) 

myarr2 = np.array([10,20,30,40,50,60,70,80,90,100]) 

ans = np.multiply(myarr1, myarr2)

print(ans)