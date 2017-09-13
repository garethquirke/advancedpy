mylist = ['north','south','west','east']

for i in range(len(mylist)):
    print(i, mylist[i])

print('')

# alternative is this:
for i,j in enumerate(mylist):
    print(i,j)

print('')

example_dict = {'left':'<','right':'>','up':'^','down':'v',}
[print(i,j) for i,j in enumerate(example_dict)]

print('')

new_dict = dict(enumerate(mylist))
print(new_dict)