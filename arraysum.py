#Hacker solution of Simple Array Sum By Riza Mohamed T
#Here is the link to the problem :- (https://www.hackerrank.com/challenges/simple-array-sum/problem)
# Get the count of numbers from the user and store it in 'n'.
n = int(input().strip())

# Get a list of numbers from the user, where each number is separated by a space.
# Convert each of these numbers to integers and store them in a list called 'arr'.
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# Calculate and print the sum of all the numbers in the list 'arr'.
print(sum(arr))
