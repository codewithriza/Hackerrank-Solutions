# Importing necessary tools
import math  
import os 
import random  
import re  # For regular expressions
import sys  

# Defining a function to find the total sum of array elements
def aVeryBigSum(ar):
    # Initial total sum is zero
    sum = 0
    
    # Going through each element in the array
    for i in range(len(ar)):
        # Adding the current element to the sum after converting it to an integer
        sum = sum + int(ar[i])
    
    # Returning the final sum
    return sum

# The main part that runs when the script is executed
if __name__ == '__main__':
    # Opening a file to store the output
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Getting the number of elements in the array
    ar_count = int(input())

    # Getting array elements and converting them to integers
    ar = list(map(int, input().rstrip().split()))

    # Calling the function to find the sum
    result = aVeryBigSum(ar)

    # Writing the result to the output file
    fptr.write(str(result) + '\n')

    # Closing the output file
    fptr.close()
