arr = [1,2,3,4]
def product_arr_except_self(arr):
  n = len(arr)
  result = [1]*n
  right = 1
  for i in range(1,n):
    result[i] = result[i-1] * arr[i -1]
  for j in range(n-1,-1,-1):
    result[j] *= right
    right *= arr[j]
  return result

# print(product_arr_except_self(arr))


# - **Time Complexity:** \( O(n) \) (two loops iterate over the array once each).  
# - **Space Complexity:** \( O(n) \) (storing the `result` array).