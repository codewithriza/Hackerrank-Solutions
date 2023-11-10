#Hey there! This is about you are in charge of the cake for a child's birthday. The cake will have one candle for each year of their total age.
#The child will only be able to blow out the tallest of the candles. Count how many candles are the tallest.
#By Riza Mohamed T

import math
import os
import random
import re
import sys

# Function to count the number of tallest candles
def countTallestCandles(candle_heights):
    tallest_count = 0  # Counter for the tallest candles
    tallest_height = max(candle_heights)  # Find the height of the tallest candle
    for height in candle_heights:
        if height == tallest_height:
            tallest_count += 1  # Increment count for each tallest candle
    return tallest_count

if __name__ == '__main__':
    # Open a file for writing the output
    output_file = open(os.environ['OUTPUT_PATH'], 'w')

    # Input the number of candles
    num_candles = int(input().strip())

    # Input the heights of the candles
    candle_heights = list(map(int, input().rstrip().split()))

    # Call the function and get the result
    result = countTallestCandles(candle_heights)

    # Write the result to the output file
    output_file.write(str(result) + '\n')

    # Close the output file
    output_file.close()
