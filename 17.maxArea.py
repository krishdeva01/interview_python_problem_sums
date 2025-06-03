height=[1,8,6,2,5,4,8,3,7]

def maxArea(height):
    left, right = 0, len(height) -1
    max_sum = 0
    while left < right:
        d = right - left
        m = min(height[right], height[left])
        if d*m > max_sum:
            max_sum = d*m
        elif height[left] < height[right]:
            left +=1
        else:
            right -=1
    return max_sum

print(maxArea(height))