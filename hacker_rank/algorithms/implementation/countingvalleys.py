# Gary is an avid hiker. He tracks his hikes meticulously, paying close
# attention to small details like topography. During his last hike, he took
# exactly steps. For every step he took, he noted if it was an uphill or a
# downhill step. Gary's hikes start and end at sea level.
#
# We define the following terms:
#     A mountain is a non-empty sequence of consecutive steps above sea level,
#     starting with a step up from sea level and ending with a step down to sea
#     level.
#
#     A valley is a non-empty sequence of consecutive steps below sea level,
#     starting with a step down from sea level and ending with a step up to sea
#     level.
#
# Given Gary's sequence of up and down steps during his last hike, find and
# print the number of valleys he walked through.
#
# Sample Input
#   8
#   UDDDUDUU
#
# Sample Output
#   1
#
# Explanation
# If we represent _ as sea level, a step up as /, and a step down as \, Gary's
# hike can be drawn as:
#
# _/\      _
#    \    /
#     \/\/
#
# It's clear that there is only one valley there, so we print 1 on a new line.

_, steps = raw_input(), raw_input()
sum = valley = 0

for step in steps:
    if step == 'U':
        sum += 1
        if sum == 0:
            valley += 1
    else:
        sum -= 1

print valley
