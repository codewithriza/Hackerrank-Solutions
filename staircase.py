# This function creates and prints a staircase of a specified size.
def staircase(n):
    # Loop through each step of the staircase.
    for i in range(1, n + 1):
        # Print '#' symbols right-aligned within a space of width n.
        print(f'{"#" * i:>{n}}')

# Check if this script is the main program.
if __name__ == '__main__':
    # Get the size of the staircase from the user.
    n = int(input().strip())
    
    # Call the staircase function with the given size.
    staircase(n)
