'''
timeit is a module used to deetermine the speed of an algorithm
speed is not a sign of effiecicy as an increased input can alter
the speed greatly instead big o notation is used to measure this accuratley.
'''
import timeit


print(timeit.timeit('1+3', number=500000))
print('')

# two functions, one is a generator the other is a list comprehension
# so which is faster?

inputs = range(100)

def divbyfive(num):
    if num % 5 == 0:
        return True
    else: return False

# generator
# mylist = list(i for i in inputs if divbyfive(i))

# list comprehension
# mylist = [i for i in inputs if divbyfive(i)]


# now lets place the code inside a timeit function
# Expected: the generator to be a lot faster

# generator
print('Generator total time')
print(timeit.timeit('''inputs = range(100)

def divbyfive(num):
    if num % 5 == 0:
        return True
    else: return False

# generator
mylist = list(i for i in inputs if divbyfive(i))''', number=500000))


print('VS.')

# list comprehension
print('List Comprehension total time')
print(timeit.timeit('''inputs = range(100)

def divbyfive(num):
    if num % 5 == 0:
        return True
    else: return False

# list comprehension
mylist = [i for i in inputs if divbyfive(i)]''', number=500000))

# In reality the two are alot closer than we would have thought
# Even with a range of 500 numbers the two are still very close
# now we will avoid the parse to list and leave it as simply a generator.

print('')

# generator without parse
print('Generator total time without parsing it to a list')
print(timeit.timeit('''inputs = range(100)

def divbyfive(num):
    if num % 5 == 0:
        return True
    else: return False

# generator
mylist = (i for i in inputs if divbyfive(i))''', number=500000))

# The results are massive... 0.03 seconds now.
# it remains a generator object thus saving time 