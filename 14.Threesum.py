
nums = [-1, 0, 1, 2, -1, -4]
def threesum(arr):
  arr.sort()
  result = []
  n = len(arr)
  if n < 3:
    return []
  for i in range(n -2):
    if arr[i] > 0:
        break
    if i > 0 and arr[i] == arr[i-1]:
      continue
    left, right = i+1, n -1
    while left < right:
      total = arr[i] + arr[left] + arr[right]
      if total == 0:
        result.append([arr[i],arr[left],arr[right]])

        while left< right and arr[left] == arr[left+1]:
          left += 1
        while left < right and arr[right] == arr[right-1]:
          right -=1
        
        left +=1
        right -=1
      elif total > 0:
        right -=1
      else:
        left +=1
  return result

print(threesum(nums))


# ### **Output:**  
# `[[-1, -1, 2], [-1, 0, 1]]` (These are the unique triplets that sum up to 0).

# ### **Time and Space Complexity:**
# - **Time Complexity:** \( O(n^2) \) (sorting the array takes \( O(n \log n) \), and the two-pointer technique inside the loop adds another \( O(n) \) for each element).
# - **Space Complexity:** \( O(n) \) (for storing the result list).