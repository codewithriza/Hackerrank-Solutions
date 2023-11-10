# Hey this is the problem .A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a given budget.
# Given price lists for keyboards and USB drives and a budget, find the cost to buy them.
# If it is not possible to buy both items, return -1.
# By Riza Mohamed T

import sys

# Taking input
s, n, m = input().strip().split(' ')
s, n, m = [int(s), int(n), int(m)]

# Taking keyboard prices as input
a = [int(keyboards_temp) for keyboards_temp in input().strip().split(' ')]

# Taking USB drive prices as input
b = [int(pendrives_temp) for pendrives_temp in input().strip().split(' ')]

# Initializing answer to -1
ans = -1

# Looping through each keyboard price
for x in a:
    # Looping through each USB drive price
    for y in b:
        # If the sum of the current keyboard and USB drive prices is less than or equal to the budget
        if x + y <= s:
            # Update the answer to the maximum of the current answer and the sum of prices
            ans = max(ans, x + y)

# Print the final answer
print(ans)
