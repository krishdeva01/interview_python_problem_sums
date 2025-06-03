nums = [10, 20, 5, 8, 30]

def second_largest(arr):
  first =  second = float("-inf")
  for num in arr:
    if num > first:
      second = first
      first = num
      if num > second and num != first:
        second = num
  return second

print(second_largest(nums))