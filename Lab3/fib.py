#! /usr/bin/python

import time
import sys

# Program to calculate the Fibonacci sequence up to n-th term
## nterms = int(input("How many terms? ")) (moved to CPU Select notebook)

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

tic = time.time()

# check if the number of terms is valid
if int(sys.argv[1]) <= 0:
   print("Please enter a positive integer")
else:
   recur_fibo(int(sys.argv[1]))
        
tac = time.time()
print('time spent: {}'.format(tac-tic))
