import numpy as np

def flat(l):
    x = l.count([])
    for i in range(x):
        l.remove([])
    print(np.sort(np.array(l).flatten()))

flat([[3, 2, 1], [4, 6, 5], [],[],[],[], [9, 7, 8]])