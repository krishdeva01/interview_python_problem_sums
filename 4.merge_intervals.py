intervals = [[1, 3], [2, 4], [6, 8], [9, 10]]

def merge_intervals(intervals):
  intervals.sort(key=lambda x: x[0])
  merged = [intervals[0]]
  for i in range(1, len(intervals)):
    if merged[-1][1] >= intervals[i][0]:
      merged[-1][1] = max(merged[-1][1], intervals[i][1])
    else:
      merged.append(intervals[i])
  return merged

print(merge_intervals(intervals)) 


# - **Time Complexity:** \( O(n \log n) \)  
# - **Space Complexity:** \( O(n) \)