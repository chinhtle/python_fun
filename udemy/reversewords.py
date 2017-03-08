# Problem:
# Given a string of words, reverse all the words.
#
# Example:
#   Given:
#     "This is the best"
#
#   Return:
#     "best the is This"
#
# Remove all leading and trailing whitespace.


def reverse_words(s):
    """
    Reverse words in a string using python specific approach.
    """
    return " ".join(s.strip().split()[::-1])


def reverse_words2(s):
    """
    Reverse words in a string using split but no built-in reversing method.
    """
    words = s.strip().split()
    n = len(words) - 1
    out = words[n]
    n -= 1

    while n >= 0:
        out = "{} {}".format(out, words[n])
        n -= 1

    return out


def reverse_words3(s):
    """
    Reverse words in a string without using split or reversing methods.
    """
    words = []
    length = len(s)

    # Parse all words. Skip spaces.
    i = 0
    while i < length:
        if s[i] != " ":
            word_start = i
            i += 1

            while i < length and s[i] != " ":
                i += 1

            words.append(s[word_start:i])

        i += 1

    n = len(words) - 1
    out = ""

    if n >= 0:
        out = words[n]
        n -= 1

        while n >= 0:
            out = "{} {}".format(out, words[n])
            n -= 1

    return out
