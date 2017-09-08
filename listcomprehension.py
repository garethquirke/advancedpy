'''
List Comprehension and Generators
---------------------------------

range() is a commonly used generator in python,
it generates values in order.

These two look quite similar so what is the difference?
- a generator creates the values on the fly, the values are created dynamically
- the amount of memory used is alot lower since it takes more time to create the list

- comprehension places the entire list into memory
- so it is faster but the penalty is memory use

when to use generators or comprehension?
 - Big list of values? generators
'''

# Generator
xyz = (i for i in range(50000000))
print(list(xyz)[:5])


# Comprehension
xyz = [i for i in range(50000000)]
print(xyz[:5])


# generator example
inputs = [4,7,9,11,3,5,8]

def divide(num):
    if num % 5 == 0:
        return True
    else: 
        return False

mylist = (i for i in inputs if divide(i))
print(list(mylist))

# here each element is cycled through the function, it's not copied in memory
# notice how it needs to be parsed into a list since it is a generator object initially


# Comprehension example
mylist = [i for i in inputs if divide(i)]
print(mylist)


# Generator expression
(x*2 for x in range(256))
for i in range(5):
    for ii in range(3):
        print(i,ii)

# List comprehension other examples
[x*2 for x in range(256)]
[print(i,ii) for ii in range(3)]
[[print(i,ii) for ii in range(3)] for i in range(5)]