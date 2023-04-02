#import class from another object
import test_3 as t

t.hello()
a,b,c,d = t.calc(36,15)
print(a)
print(b)
print(c)
print(d)

#import specific func and give it another name
from test_3 import hello as greet

greet()