def merge_sort(arr):
  if len(arr) <=1:
    return arr
  
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  return merge(left, right)

def merge(left, right):
  i,j=0,0
  arr = []

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr.append(left[i])
      i +=1
    else:
      arr.append(right[j])
      j += 1

  arr.extend(left[i:])
  arr.extend(right[j:])
  return arr
arr = [8,5,6,7,3,5,4,1,2]
print(merge_sort(arr))

### **Time and Space Complexity for Merge Sort:**

# - **Time Complexity:** \( O(n \log n) \)  
#   - The array is repeatedly divided into halves (\( \log n \) levels), 
# and merging takes \( O(n) \) at each level.

# - **Space Complexity:** \( O(n) \)  
#   - Temporary arrays are used during merging, and 
# the recursion stack consumes additional space.