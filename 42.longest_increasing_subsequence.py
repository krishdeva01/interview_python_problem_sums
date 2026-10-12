"""
42. Longest Increasing Subsequence (length)
Length of the longest strictly increasing subsequence.

Approach (patience sorting): keep `tails`, where tails[i] = smallest tail of an
increasing subsequence of length i+1. For each number, binary-search its slot
(leftmost tail >= x) with a hand-written binary search — no library needed.
Time: O(n log n)   Space: O(n)

Shortcut: "for x: find leftmost tail >= x; replace it, or append if none.
           answer = len(tails)."
"""


def length_of_lis(nums):
    tails = []
    for x in nums:
        # binary search: leftmost index i where tails[i] >= x
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(tails):
            tails.append(x)     # x extends the longest run
        else:
            tails[lo] = x       # x is a smaller tail for that length
    return len(tails)


if __name__ == "__main__":
    # Input: [10, 9, 2, 5, 3, 7, 101, 18]
    print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))   # Output: 4  (2,3,7,101)
