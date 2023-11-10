#!/bin/python3

# Problem: Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with 6 places after the decimal.
#By Riza Mohamed T

# This function calculates and prints the ratios of positive, negative, and zero elements in an array.
def plusMinus(arr):
    # Initialize counters for positive, negative, and zero elements.
    positiveCounter = 0
    negativeCounter = 0
    zeroCounter = 0

    # Iterate through the array to count positive, negative, and zero elements.
    for i in range(len(arr)):
        if arr[i] > 0:
            positiveCounter += 1
        elif arr[i] < 0:
            negativeCounter += 1
        else:
            zeroCounter += 1

    # Calculate and print the proportion of positive values with 6 decimal places.
    print(f"{positiveCounter / len(arr):.6f}")
    # Calculate and print the proportion of negative values with 6 decimal places.
    print(f"{negativeCounter / len(arr):.6f}")
    # Calculate and print the proportion of zero values with 6 decimal places.
    print(f"{zeroCounter / len(arr):.6f}")

# The main block of code that takes input, creates an array, and calls the plusMinus function.
if __name__ == '__main__':
    # Take input for the size of the array.
    n = int(input().strip())

    # Take input for the array elements and convert them to integers.
    arr = list(map(int, input().rstrip().split()))

    # Call the plusMinus function with the provided array.
    plusMinus(arr)
