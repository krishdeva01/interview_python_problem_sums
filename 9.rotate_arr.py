arr = [1,2,3,4,5]

def rotate_arr(arr, k):
  n = len(arr)
  k %= n
  return arr[-k:] + arr[:-k]
print(rotate_arr(arr, 3))


# ### **Output:**  
# `[3, 4, 5, 1, 2]` (The array is rotated 3 positions to the right).

# ### **Time and Space Complexity:**
# - **Time Complexity:** \( O(n) \) (because slicing the array and concatenating takes linear time).
# - **Space Complexity:** \( O(n) \) (a new array is created to store the rotated result).