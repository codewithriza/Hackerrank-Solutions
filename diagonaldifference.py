# Hey , Here it is given a square matrix, we have to calculate the absolute difference between the sums of its diagonals.
#By Riza Mohamed T
#!/bin/python3

# Importing necessary libraries
import math
import os
import random
import re
import sys

# Function to calculate the absolute difference between the sums of diagonals
def diagonalDifference(arr):
    # Calculate the sum of the left-to-right diagonal
    d1 = sum([arr[x][x] for x in range(len(arr))])
    
    # Calculate the sum of the right-to-left diagonal
    d2 = sum([arr[x][len(arr) - 1 - x] for x in range(len(arr))])
    
    # Return the absolute difference between the two diagonal sums
    return abs(d1 - d2)

# Main function
if __name__ == '__main__':
    # Open a file for writing the output
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Input: Number of rows and columns in the square matrix
    n = int(input().strip())

    # Initialize an empty matrix
    arr = []

    # Input: Elements of the matrix row by row
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Call the function to calculate diagonal difference
    result = diagonalDifference(arr)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()
