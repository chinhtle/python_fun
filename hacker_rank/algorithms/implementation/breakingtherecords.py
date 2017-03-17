# Maria plays n games of college basketball in a season. Because she wants to
# go pro, she tracks her points scored per game sequentially in an array
# defined as scores = [s0, s1, ..., sn-1]. After each game i, she checks to see
# if score si breaks her record for most or least points scored so far during
# that season.
#
# Given Maria's array of scores for a season of n games, find and print the
# number of times she breaks her record for most and least points scored during
# the season.
#
# Note: Assume her records for most and least points at the start of the season
# are the number of points scored during the first game of the season.
#
# Input Format:
# The first line contains an integer denoting n (the number of games).
# The second line contains n space-separated integers describing the respective
# values of .
#
# Constraints:
#   1 <= n <= 1000
#   0 <= si <= 10^8
#
# Output Format:
# Print two space-separated integers describing the respective numbers of times
# her best (highest) score increased and her worst (lowest) score decreased.

raw_input()  # Not needed
scores = map(int, raw_input().split())

lowest = highest = scores[0]
lowest_count = highest_count = 0

for score in scores[1:]:
    if score > highest:
        highest = score
        highest_count += 1
    elif score < lowest:
        lowest = score
        lowest_count += 1

print highest_count, lowest_count
