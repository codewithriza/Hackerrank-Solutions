# Problem: Compare Alice and Bob's challenge ratings
#By Riza Mohamed T


# Input: Alice's challenge rating
a = list(map(int, input().split()))

# Input: Bob's challenge rating
b = list(map(int, input().split()))

# Initialize scores for Alice and Bob
alice_score = 0
bob_score = 0

# Compare ratings for each category
for i in range(3):
    # Compare category ratings for Alice and Bob
    if a[i] > b[i]:
        # If Alice's rating is higher, she gets a point
        alice_score += 1
    elif a[i] < b[i]:
        # If Bob's rating is higher, he gets a point
        bob_score += 1

# Output the scores
print(alice_score, bob_score)
