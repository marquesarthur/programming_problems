import math
import os
import random
import re
import sys


# Complete the romanizer function below.
def romanizer(numbers):
    pass



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(raw_input())

    numbers = []

    for _ in xrange(numbers_count):
        numbers_item = int(raw_input())
        numbers.append(numbers_item)

    res = romanizer(numbers)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()
