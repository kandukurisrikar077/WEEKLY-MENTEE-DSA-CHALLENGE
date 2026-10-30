def leadersinarray(arr):
    n=len(arr)
    res=[arr[n-1]]
    max_right = arr[n-1]
    for right in range(n-2,-1,-1):
        if(arr[right])> max_right:
            res.append(arr[right])
            max_right=arr[right]
    return (res[::-1])
arr=list(map(int,input("Enter array elements: ").split()))
result=leadersinarray(arr)
print("Leaders in the array:", result)