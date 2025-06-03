# Online Python compiler (interpreter) to run Python online.
cost = [1,100,1,1,1,100,1,1,100,1]

def maxCost(arr):
    l = 0
    n = len(arr) -1
    sm = min(arr[0], arr[1])
    while l < n:
        if arr[l] < arr[l+1]:
            sm += arr[l+1]
            l+1
        else:
            sm +=arr[l+2]
            l +=2
    return sm
print(maxCost(cost))