# Hey there! This is a simple Python script to find the minimum and maximum sums
# of four out of five integers in a list.
#By Riza Mohamed T

# Let's define a function named miniMaxSum that takes a list of integers as input.
def miniMaxSum(arr):
    
    # Sort the list in ascending order.
    arr = sorted(arr)
    
    # Print the sum of all elements except the last one (minimum sum)
    # and the sum of all elements except the first one (maximum sum).
    print(sum(arr[:-1]), sum(arr[1:]))

# This block is a common Python idiom to check if the script is being run as the main program.
if __name__ == '__main__':
    
    # Get a list of integers as input from the user, splitting the input string at spaces.
    arr = list(map(int, input().rstrip().split()))

    # Call the miniMaxSum function with the input list.
    miniMaxSum(arr)
