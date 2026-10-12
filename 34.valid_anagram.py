"""
34. Valid Anagram
An anagram uses the EXACT same letters, just reordered.
Return True if t is an anagram of s.

Idea: if you sort both words, anagrams turn into identical strings.
      "anagram" -> "aaagmnr"
      "nagaram" -> "aaagmnr"   -> equal, so it's an anagram.
Time: O(n log n)   Space: O(n)

Code to remember:
    return sorted(s) == sorted(t)
"""


def is_anagram(s, t):
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    # Input: s = "anagram", t = "nagaram"
    print(is_anagram("anagram", "nagaram"))   # Output: True

    # Input: s = "rat", t = "car"
    print(is_anagram("rat", "car"))           # Output: False
