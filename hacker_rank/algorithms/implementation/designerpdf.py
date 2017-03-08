# When you select a contiguous block of text in a PDF viewer, the selection is
# highlighted with a blue rectangle. In a new kind of PDF viewer, the
# selection of each word is independent of the other words; this means that
# each rectangular selection area forms independently around each highlighted
# word.
#
# In this type of PDF viewer, the width of the rectangular selection area is
# equal to the number of letters in the word times the width of a letter, and
# the height is the maximum height of any letter in the word.
#
# Consider a word consisting of lowercase English alphabetic letters, where
# each letter is 1mm wide. Given the height of each letter in millimeters (mm),
# find the total area that will be highlighted by blue rectangle in mm^2 when
# the given word is selected in our new PDF viewer.
#
# Input Format:
# The first line contains 26 space-separated integers describing the
# respective heights of each consecutive lowercase English letter
# (i.e., ha, hb, hc, ..., hy, hz).
# The second line contains a single word, consisting of lowercase English
# alphabetic letters.
#
# Constraints:
#   - 1 <= h? <= 7, where ? is an English lowercase letter.
#   - Word contains no more than 10 letters.
#
# Output Format:
# Print a single integer denoting the area of highlighted rectangle when the
# given word is selected. The unit of measurement for this is square
# millimeters (mm^2), but you must only print the integer.
#
# Sample Input:
#   1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
#   abc
#
# Sample Output:
#   9
#
# Explanation:
# We are highlighting the word abc:
#   The tallest letter in abc is b, and hb = 3. The selection area for this
#   word is 3 * 1mm * 3mm = 9mm^2.
#
# Note: Recall that the width of each character is 1mm.

heights = map(int, raw_input().split())
word = raw_input()

max_height = 0
for ch in word:
    max_height = max(heights[ord(ch) - ord('a')], max_height)

print len(word) * max_height
