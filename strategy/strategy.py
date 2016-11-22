#!/usr/bin/env python
# coding=utf-8

LIMIT = 5
WARNING = 'Bad algorithm'

def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i],seq[(i+1)%n]

class AllUnique(object):
    def allUniqueSort(self, seq):
        if len(seq)>LIMIT:
            print(WARNING)
        sortStr = sorted(seq)
        for (c1, c2) in pairs(sortStr):
            if c1 == c2:
                return False
        return True
    
    def allUniqueSet(self, seq):
        if len(seq)<LIMIT:
            print(WARNING)
        return True if len(set(seq))==len(seq) else False  

def main():
    seq1 = 'abcdadc'
    strategy_picked = input('Choose strategy: [1] use a set, [2] Sort and pair>')
    uniqClass = AllUnique()
    if strategy_picked == 1:
        return uniqClass.allUniqueSet(seq1)
    elif strategy_picked == 2:
        return uniqClass.allUniqueSort(seq1)
    else:
        raise Exception('Choose strategy [1] or [2]')

if __name__ == "__main__":
    output = main()
    print('{}'.format(output))


