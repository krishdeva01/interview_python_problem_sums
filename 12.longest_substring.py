value = 'abcdbda'
def longest_substring(value):
  res_set = set()
  l=0
  max_num = 0
  for i in range(0, len(value)):
    while value[i] in res_set:
      res_set.remove(value[l])
      l += 1
    res_set.add(value[i])
    max_num = max(max_num, i -l + 1)
  return max_num
print(longest_substring(value))


# ### **Output:**  
# `4` (The longest substring without repeating characters is `'abcd'`).

# ### **Time and Space Complexity:**
# - **Time Complexity:** \( O(n) \) (two pointers traverse the string, where \( n \) is the length of the string).
# - **Space Complexity:** \( O(n) \) (due to the set used to store unique characters).