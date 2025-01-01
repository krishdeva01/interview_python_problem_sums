arr = [1,2,3,4,5,6]
target = 3
def twosumII(arr,target):
  i,j = 0, len(arr) -1
  while i<j:
    if arr[i] + arr[j] == target:
      return [i,j]
    elif arr[i] + arr[j] > target:
      j -=1
    else:
      i +=1

print(twosumII(arr, target))


# ### **Output:**  
# `[-1]` (No two numbers in the array sum up to 110).

# ### **Time and Space Complexity:**
# - **Time Complexity:** \( O(n) \) (the two-pointer technique allows us to traverse the array once).
# - **Space Complexity:** \( O(1) \) (no extra space used apart from a few variables).