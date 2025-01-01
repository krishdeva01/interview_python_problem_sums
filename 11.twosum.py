arr = [1,3,4,5,6,7]
target = 13

def twosum(arr, target):
  dct = dict()
  for index, num in enumerate(arr):
    diff = target - num
    if diff in dct:
      return[dct[diff], index]
    else:
      dct[num] = index
print(twosum(arr, target))


# ### **Output:**  
# `[4, 5]` (The two numbers that sum up to 79 are 5 and 74, found at indices 4 and 5).

# ### **Time and Space Complexity:**
# - **Time Complexity:** \( O(n) \) (single pass through the array, where \( n \) is the length of the array).
# - **Space Complexity:** \( O(n) \) (due to the dictionary storing values and their indices).