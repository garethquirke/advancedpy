# assume input is 10 and rows is 4

def triangleCreator(num,rows):
    r = 1
    while r != (rows + 1):
        x = str(round((num / r) ,2))
        x += ' '
        print(str(x)*r)
        r+=1
    print('\n')


triangleCreator(100,4)
triangleCreator(400,2)
triangleCreator(600,3)
triangleCreator(120,5)
triangleCreator(40,4)
triangleCreator(50,10)