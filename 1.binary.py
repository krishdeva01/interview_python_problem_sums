nums = [1,2,3,4,5,67]

def binary(nums, target):
  low=0
  high = len(nums) - 1
  while low <= high:
    mid = (low+high) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      low  = mid + 1
    else:
      high = mid -1
  return -1

print(binary(nums, 67))


### **Time and Space Complexity:**
# - **Time Complexity:** \( O(\log n) \) (halves the search space in each iteration).  
# - **Space Complexity:** \( O(1) \) (no additional space is used).