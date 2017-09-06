import os.path

names = ['jim','gg','bob','timmer']

for name in names:
    statement = 'hello there ' + name
    print(statement)

print('\n')

for name in names:
    statement = ' '.join(['hello there ', name])
    print(statement)

print('\n')

# file path examples
path = 'C:/Users/Gareth/Files'
filename = 'city.h'

print(os.path.join(path, filename))

# formatting
who = 'gareth'
what = 'lambos'
quantity = 30

print('\n')

print('{} bought {} {} today.'.format(who,quantity,what))