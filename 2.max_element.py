def largest(arr, n):
    mx = arr[0]
    for i in range(1, n):
        if arr[i] > mx:
            mx = arr[i]

    return mx

if __name__ == '__main__':
    arr = [10, 324, 45, 90, 9808]
    n = len(arr)
    
    ans = largest(arr, n)
    
    print(ans)

# - **Time Complexity:** \( O(n) \) (as it iterates through the array once).  
# - **Space Complexity:** \( O(1) \) (no additional space is used).