Negative index is used in python to index starting from the last element of the list, 
tuple or any other container class which supports indexing.
-1 refers to the last index, -2 refers to the second last index and so on.
	for example -(s[::-1])
	

#memory management 
Memory management in Python involves a private heap containing all Python objects and data structures. 
The management of this private heap is ensured internally by the Python memory manager. 
The Python memory manager has different components which deal with various dynamic storage management 
aspects, like sharing, segmentation, preallocation or caching.




#When manipulating lists, you have access to two methods called append() and extend()
#Append object at the end 
x = [1, 2, 3]
x.append([4, 5])
print (x)
gives you: [1, 2, 3, [4, 5]]

# Extends list by appending elements from the iterable.

x = [1, 2, 3]
x.extend([4, 5])
print (x)
gives you: [1, 2, 3, 4, 5]

#Mutable and Immutable
mutable data structure is the structred which can be changed eg-list ,dictionary,set 
x=[1,2,3,4,5,45,6]
x[3]="riyaz" #which is string
x
[1,2,3"riyaz",5,6]

Immutable 
data structure which cannont be changed for eg -frozen set,tuple 
frozenset([1,2,3])


negative index 
Negative index is used in python to index starting from the last element of the list, tuple or any other container class which supports indexing. -1 refers to the last index, -2 refers to the second last index and so on.

For lists :

x = [0,1,2,3,4,5]

x[-1]

5

For strings :

string = "Hello!"

string[-1]

'!'


Difference between Xrange and range 
range() and xrange() are two functions that could be used to iterate a certain number of times in 
for loops in Python. In Python 3, there is no xrange , but the range function behaves like xrange
 in Python 2.If you want to write code that will run on both Python 2 and Python 3, you should use range().
range()
range() returns – the list as return type.
# initializing a with range() 
a = range(1,10000) 
  
xrange() returns – xrange() object.
# initializing a with xrange() 
x = xrange(1,10000) 



