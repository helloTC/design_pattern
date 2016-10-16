#!/usr/bin/env python
# coding=utf-8

import functools

def memoize(fn):
    known = dict()
    
    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer

@memoize
def fibonacci(n):
    assert (n>=0), 'n must be >= 0'
    return n if n in (0,1) else fibonacci(n-1)+fibonacci(n-2)

@memoize
def fsum(n):
    assert (n>=0), 'n must be >=0'
    return 0 if n == 0 else fsum(n-1) + n

if __name__ == '__main__':
    # from timeit import Timer
    measure = [{'exec':'fibonacci(100)', 'import':'fibonacci',
                'func':fibonacci},{'exec':'fsum(200)', 
                'import':'fsum', 'func':fsum}]
    for m in measure:
        print('name: {}, doc: {}'.format(m['func'].__name__, m['func'].__doc__)) 
