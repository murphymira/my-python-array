 import array as arr
 # a is variable,first array is the name of integer module,the second array is the array constructor
a = arr.array('i',[1,2,3,4,5,6])
print(a)

#  second method
import array as array
# a is variable,first array is the name of integer module,the second array is the array constructor
a = array.array('i',[1,2,3,4,5,6])
print(a)

# third method
from array import *
# a is variable,first array is the name of integer module,the second array is the array constructor
a = array('i',[1,2,3,4,5,6])
print(a)

# accessing array elements

from array import *

 # a is variable,first array is the name of integer module,the second array is the array constructor
a = array('i', [1, 2, 3, 4, 5, 6])
i = a[1]
print(i)

# finding the length of an array
import array as arr

a = [1.2, 2.3, 3.4, 4.5, 5.6, 6.6]
x = len(a)
print(x)

# adding element to an array

import array as arr

a = arr.array('d', [1.1, 2.1, 3.1])
a.append(4.1)
print("array a=",a)

import array as arr
a = [1.1, 2.1, 3.1]
a.append(4.1)
print(a)
import array as arr
b = arr.array('d', [1.1, 2.1, 3.1])
b.extend([4.1 ,5.6 ,6.7])
print("array b=",b)

import array as arr

b = [1.1, 2.1, 3.1]
b.extend([4.1, 5.6, 6.7])
print(b)
import array as arr
c = arr.array('d', [1.1, 2.1, 3.1])
c.insert(2,3.4)
print("Arrays c=",c)

c = [1.1, 2.1, 3.1]
c.insert(2,3.4)
print(c)

# adding Element
e = [1, 2, 3, 4, 5, 6, 7]
e.append(8)
print("Array of this python =", e)

e = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
e.append(9)
print("Array of e =", e)

# removing element
f = [1, 2, 3, 4, 5, 6, 7]
e.remove(6)
print("i remove this array number which is =",e)

a=arr.array('d',[1.1, 2.2, 3.8,3.1,3.7])
print("popping last element",a.pop())
print("popping 4th element",a.pop(3))
a.remove(1.1)
print(a)

import array as arr

a = arr.array('i',[1,2,6,4,5,6,7,8])
a.pop(2)
print(a)
a = [1,2,6,4,5,6,7,8]
a.pop(6)
print(a)

# concatenation
import array as arr
a = arr.array('d',[1.1 ,2.1 ,3.1, 2.6,7.8])
b = arr.array('d',[3.7,8.6])
c = arr.array('d')
c = a + b
print("Array c = ",c)

import array as arr
a = [1.1 ,2.1 ,3.1, 2.6,7.8,6,9]
b = [3.7,8.6]
c = a + b
print("Array concatination is =",c)

import array as arr
a = arr.array('d',[1.1, 2.1 ,3.1 ,2.6 ,7.8])
print(a[0:3])

import array as arr
a= [1.1, 2.1, 3.1, 2.6, 7.8, 3.7, 8.6]
print(a[0:-2])

# looping through an Array using for loop

import array as arr
a = arr.array('d',[1.1, 2.1, 3.1, 2.6, 7.8, 3.7, 8.6])
print("All values")
for x in a:
    print(x)

import array as arr
a = [1,2,3,4,5,6,7,8,9,10,11,12]
for x in a:
    print(x)

# looping through an array using while loop
import array as arr
a=arr.array('d', [1.1, 2.1, 3.1,4.1, 5.1])
b = 0

while b < len(a):
    print(a[b])
    b = b+1

temp = 0










