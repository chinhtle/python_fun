# Monica wants to buy one keyboard and one USB drive from her favorite
# electronics store. The store sells n different brands of keyboards and m
# different brands of USB drives. Monica has exactly s dollars to spend, and
# she wants to spend as much of it as possible (i.e., the total cost of her
# purchase must be maximal).
#
# Given the price lists for the store's keyboards and USB drives, find and
# print the amount money Monica will spend. If she doesn't have enough money
# to buy one keyboard and one USB drive, print -1 instead.
#
# Note: She will never buy more than one keyboard and one USB drive even if she
# has the leftover money to do so.
#
# Input Format:
# The first line contains three space-separated integers describing the
# respective values of s (the amount of money Monica has), n (the number of
# keyboard brands) and m (the number of USB drive brands).
# The second line contains n space-separated integers denoting the prices of
# each keyboard brand.
# The third line contains m space-separated integers denoting the prices of
# each USB drive brand.
#
# Constraints:
#   1 <= n, m <= 1000
#   1 <= s <= 10^6
#   The price of each item is in the inclusive range [1, 10^6].
#
# Output Format:
# Print a single integer denoting the amount of money Monica will spend. If she
# doesn't have enough money to buy one keyboard and one USB drive, print -1
# instead.
#
# Sample Input 0
#   10 2 3
#   3 1
#   5 2 8
#
# Sample Output 0
#   9
#
# Explanation 0
# She can buy the 2nd keyboard and the 3rd USB drive for a total cost
# of 8 + 1 = 9.
#
# Sample Input 1
#   5 1 1
#   4
#   5
#
# Sample Output 1
#   -1
#
# Explanation 1
# There is no way to buy one keyboard and one USB drive because 4 + 5 > 5,
# so we print -1.
#
# Use a brute-force approach to solve the problem.

s = map(int, raw_input().strip().split())[0]
keyboards = map(int, raw_input().strip().split())
pendrives = map(int, raw_input().strip().split())

max_spent = -1
for kb in keyboards:
    for pd in pendrives:
        total = kb + pd
        if total <= s:
            max_spent = max(max_spent, total)

print max_spent
