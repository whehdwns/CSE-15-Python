# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:47:47 2018

@author: whehdwns
"""

# 1.1 AND (p and q)
def AND(p, q):
    return p and q


# 1.2 OR (p or q)
def OR(p, q):
    return p or q


# 1.3 IF (p -> q)
def IF(p, q):
    return not p or q


# 1.4 NOT (-p)
def NOT(p):
    return not p


# 1.5 IFF (p <-> q)
def IFF(p, q):
    return IF(p, q) and IF(q, p)


# 1.6
# Give a prefix representation of a proposition, of the form prop = ('OR', True, False)
# Write a function named evaluate, which will evaluate the proposition
# You should use the functions defined in question 1
def evaluate(formula):
    a = formula[0]
    if (a == 'AND'):
        return AND(formula[1], formula[2])
    if (a == 'OR'):
        return OR(formula[1], formula[2])
    if (a == 'IF'):
        return IF(formula[1], formula[2])
    if (a == 'NOT'):
        return NOT(formula[1])
    if (a == 'IFF'):
        return IFF(formula[1], formula[2])
   #Test your evaluation functionwith the following:
    print ("Simple Evaluation Function Test")
    print
    p = True
    q = False

    print ("p =", p)
    print ("q =", q)

    print
    print ("(p or q):   ", evaluate(('OR', p, q)))
    print ("(p and q):  ", evaluate(('AND', p, q)))
    print ("(p -> q):   ", evaluate(('IF', p, q)))
    print ("(p <-> q):  ", evaluate(('IFF', p, q)))
    print ("-p:         ", evaluate(('NOT', p)))
