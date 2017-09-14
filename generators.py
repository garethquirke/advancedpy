'''
This file is the non lazy way to write a generator
it is important to know how to write a generator this way.
'''

def simplegenerator():
    yield 'oh'
    yield 'what'
    yield 'you'
    yield 'got'
    yield 'there'

for i in simplegenerator():
    print(i)

'''
Excercise: 
Find the combination of the lock when the correct combo is: 365

first case we will do this in the standard way iteratively,
next we will show how it can be made easier with generators.
'''

CORRECT_COMBO = (3, 6, 1)

for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print('Found the combo:{}'.format((c1, c2, c3)))
                break # this prevents the code from iterating through the rest of the loop


found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print('Found the combo:{}'.format((c1, c2, c3)))
                found_combo = True
                break


# combo broken through a generator
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo:{}'.format((c1, c2, c3)))
        break

'''
Todo: add comments
'''