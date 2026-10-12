"""
40. House Robber
Max money you can rob without robbing two adjacent houses.

Approach: DP rolling — at each house choose max(skip it, rob it + best two back).
Time: O(n)   Space: O(1)

Shortcut: "prev2, prev1 = 0, 0; cur = max(prev1, prev2 + num); roll."
"""


def rob(nums):
    prev2 = prev1 = 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1


if __name__ == "__main__":
    print(rob([2, 7, 9, 3, 1]))   # Output: 12  (rob 2 + 9 + 1)
    print(rob([2, 1, 1, 2]))      # Output: 4   (rob 2 + 2)
