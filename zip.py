a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = ['a','b','d','e','f']

# The zip function allows us iterate through these two 
# lists and aggregates them.

# for a,b in zip(a,b):
#   print(a,b)

# Now lets do it with another list.
c = ['a','b','d','e','f']

for a,b,c in zip(a,b,c):
    print(a,b,c)

# notice: we had to comment out the above code as it would not run
# twice. Zip creates a zip object thus revoking our ability to run
# it once again on the same list.

list1 = [ 'a' , 'b' ]
list2 = [ 1, 2 ]
print(zip(list1, list2))
# output: <zip object at 0x000001BAAB98CFC8>
