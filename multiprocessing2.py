'''
In this py we will use multiproccessing to do a job and return 
the results back to a main function
'''
import threading
from multiprocessing import Pool
# pool allows us to create a pool of worker processes 
# lets run a function over a list of nums

def job(num):
    return num * 2

if __name__ == '__main__':
    p = Pool(proccesses=10)
    numbers = p.map(job, [i for i in range(10)])
    p.close()
    print(numbers)


