#! /usr/bin/python

import ctypes
import time
import sys
func = ctypes.CDLL('./libMyLib.so')
# Program to calculate the Fibonacci sequence up to n-th term
## nterms = int(input("How many terms? ")) (moved to CPU Select notebook)
func.initPMU()
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

tic = time.time()
beforeC = func.getCyclecount()

# check if the number of terms is valid
if int(sys.argv[1]) <= 0:
   print("Please enter a positive integer")
else:
   recur_fibo(int(sys.argv[1]))
        
tac = time.time()
afterC = func.getCyclecount()
cycleTotal = afterC - beforeC

print('time spent: {}'.format(tac-tic))
print('cycles spent: {}'.format(cycleTotal))
