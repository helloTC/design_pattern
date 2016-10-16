#!/usr/bin/env python
# coding=utf-8
known1 = {0:0, 1:1}
known2 = {1:1}

def fibonacci(n):
    assert(n>=0), 'n must be >=0'
    if n in known1:
        return(known1[n])
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
        known1[n] = res
        return res

def fsum(n):
    assert(n>=0), 'n must be >=0'
    if n in known2:
        return(known2[n])
    else:
        res = fsum(n-1) + n
        known2[n] = res
    return res

