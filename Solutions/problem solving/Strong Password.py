#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    y='!@#$%^&*()-+'
    x=0
    if(any(i.isdigit()for i in password)==False):
        x+=1
    if(any(i.islower()for i in password)==False):
        x+=1
    if(any(i.isupper()for i in password)==False):
        x+=1
    if(any(i in y for i in password)==False):
        x+=1
    print(max(x,6-n))

    

    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

