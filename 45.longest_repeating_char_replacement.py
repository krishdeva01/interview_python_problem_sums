"""
45. Longest Repeating Character Replacement
Longest substring where you can replace at most k characters so all chars match.

Approach: sliding window; window is valid while
(window_length - count_of_most_frequent_char) <= k.
Time: O(n)   Space: O(1)  (<=26 letters)

Shortcut: "grow right; if (len - maxFreq) > k: shrink left; track best."
"""


def character_replacement(s, k):
    count = {}                       # plain dict instead of defaultdict
    left = best = max_freq = 0
    for right, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1
        max_freq = max(max_freq, count[ch])
        if (right - left + 1) - max_freq > k:   # too many replacements needed
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    # Input: s = "AABABBA", k = 1
    print(character_replacement("AABABBA", 1))   # Output: 4  (e.g. "AABA"->"AAAA")
