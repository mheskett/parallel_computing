"""
Elliot and Mike testing out parallel computing in python
"""

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))

"""
shit
"""
