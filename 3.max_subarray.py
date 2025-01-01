arr = [2, 3, -8, 7, -1, 2, 3]

def max_subarray(arr):
  max_sum = float("-inf")
  current_sum = 0
  for i in arr:
    current_sum += i
    max_sum = max(max_sum, current_sum)
    if current_sum < 0:
      current_sum = 0
  return max_sum

print(max_subarray(arr))


# The code implements **Kadane's Algorithm** to find the maximum sum of a contiguous subarray in the given array.

# ### **Output:**  
# `11` (The maximum sum subarray is `[7, -1, 2, 3]`).

# ### **Time and Space Complexity:**
# - **Time Complexity:** \( O(n) \) (traverses the array once).
# - **Space Complexity:** \( O(1) \) (no additional space is used).