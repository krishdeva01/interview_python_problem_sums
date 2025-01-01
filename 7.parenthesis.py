value = "(()[){]}"
def valid_parenthesis(value):
  st = []
  d = {")":"(", "]":"[", "}":"{"}
  for char in value:
    if char in d.keys():
      if st and st[-1] == d[char]:
        st.pop()
      else:
        return False
    else:
      st.append(char)

  return not st
print(valid_parenthesis(value))
      

# ### Output:
# `False` (The parentheses in `"(()[){]}"` are not balanced).

# ### **Time and Space Complexity:**
# - **Time Complexity:** \( O(n) \) (where \( n \) is the length of the string, as we iterate through it once).  
# - **Space Complexity:** \( O(n) \) (in the worst case, all characters are opening brackets and stored in the stack).