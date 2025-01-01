arr = [5,3,4,7,8,9,1,2]

def quick_sort(arr):
  if len(arr) <=1:
    return arr
  pivot = arr[len(arr)//2]
  left = [x for x in arr if x < pivot]
  mid = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]

  return quick_sort(left) + mid + quick_sort(right)

print(quick_sort(arr))


# ### **Output:**  
# `[1, 2, 3, 4, 5, 7, 8, 9]` (The array is sorted using Quick Sort).

# ### **Time and Space Complexity:**
# - **Time Complexity:**
#   - **Average case:** \( O(n \log n) \) (the pivot divides the array roughly in half each time).
#   - **Worst case:** \( O(n^2) \) (when the pivot is always the smallest or largest element, leading to unbalanced partitions).
  
# - **Space Complexity:** \( O(n) \) (due to the space used by the left, mid, and right subarrays).