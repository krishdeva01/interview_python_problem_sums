arr = [1,2,3,4,6]
def find_missing_num(arr):
  actual_sum = sum(arr)
  n = len(arr) + 1
  expected_sum = n * (n+1)//2
  return expected_sum - actual_sum 

print(find_missing_num(arr))

# ### **Output:**  
# `5` (The missing number in the array is `5`).

# ### **Time and Space Complexity:**
# - **Time Complexity:** \( O(n) \) (summing the elements of the array).  
# - **Space Complexity:** \( O(1) \) (no additional space used).