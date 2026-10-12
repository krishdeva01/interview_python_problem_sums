"""
36. Contains Duplicate
True if any value appears at least twice.

Approach: a set drops duplicates, so compare lengths.
Time: O(n)   Space: O(n)

Shortcut: "len(set(nums)) != len(nums)."
"""


def contains_duplicate(nums):
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))   # Output: True
    print(contains_duplicate([1, 2, 3, 4]))   # Output: False
