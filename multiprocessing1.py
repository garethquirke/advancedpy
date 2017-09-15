'''
GIL: Global Interpreter Lock
This is a memory management safegaurd.
Python is a single threaded language, so even if you use threads it
will sill run on a single CPU. SO your computer could have 4 cores
your computer is fooled into believing it has 8 through threads.
Threading allows us to access idle threads, its not using more power,
it is simly using threads that are not in use. 

This multiproccessing module allows us to use full concurrency ie running
multiple python scripts at the one time even though it is just the one script.
If we look at the current list of processes we will see lots of python in the ongoing
section. 

Because we're using separate processes, we're, in a sense, circumventing the GIL.
Each process is subject to the GIL still, but, if you can figure out how to parallelize
your process, you're going to see major performance improvements.
'''

import multiprocessing

def spawn():
    print('Spawned')

if __name__ == '__main__':
    for i in range(100):
        p = multiprocessing.Process(target=spawn)
        p.start()
        # p.join()

def spawn(num):
    print('Spawn # {}'.format(num))

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()

def spawn(num, num2):
    print('Spawn # {} {}'.format(num, num2))

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn, args=(i, i+1))
        p.start()