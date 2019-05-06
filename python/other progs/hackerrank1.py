# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 21:52:23 2019

@author: praveen
"""
#understood way
def solveMeFirst(a,b):
    return a+b
	# Hint: Type return a+b below
    num1 = int(input(2))
    num2 = int(input(3))
    res = solveMeFirst(num1,num2)
    print(res)
solveMeFirst(2,3)

#real way
def solveMeFirst(a,b):
	# Hint: Type return a+b below
  return a+b
num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)


#####hckerrank 2 task



#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    for i in ar[6, 1, 2, 3, 4, 10, 11]:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

<<

a=50
def func(a):
    print('a is', a)
    a=2
    print('changed locala to ', a)
func(a)
print('a is atill',a)

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )

print tuple[0]