#!/usr/bin/python

# Problem: Check if two strings are anagrams of each other.
# Assume all lower cased and no spaces.


def anagram(s1, s2):
    """
    Anagram check with purely using python specific approach.
    """
    return sorted(s1) == sorted(s2)


def anagram2(s1, s2):
    """
    Anagram check while minimizing the usage of python specific approaches.
    """
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for value in count.values():
        if value != 0:
            return False

    return True
