"""
35. Group Anagrams
Put words that are anagrams of each other into the same group.

Idea: anagrams share the SAME sorted letters. Use the sorted word as a
      dictionary key (the "label on the box") and drop each word in its box.
      "eat", "tea", "ate"  all sort to "aet"  -> same box.
Time: O(n * k log k)   Space: O(n * k)   (n words, k = word length)

Code to remember:
    groups = {}
    for w in strs:
        key = "".join(sorted(w))
        if key not in groups: groups[key] = []
        groups[key].append(w)
    return list(groups.values())
"""


def group_anagrams(strs):
    groups = {}
    for w in strs:
        key = "".join(sorted(w))       # "tea" -> "aet"
        if key not in groups:
            groups[key] = []
        groups[key].append(w)
    return list(groups.values())


if __name__ == "__main__":
    # Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

