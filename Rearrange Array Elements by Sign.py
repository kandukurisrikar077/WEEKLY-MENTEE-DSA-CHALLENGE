def RearrangeArrayElementsbySign(arr):
    n = len(arr)
    pos = 0
    neg = 1
    res = [0] * n
    for right in range(n):
        if arr[right] > 0:
            res[pos] = arr[right]
            pos +=2
        else:
            res[neg] = arr[right]
            neg +=2

    return res
arr=list(map(int,input("Enter array elements: ").split()))
result=RearrangeArrayElementsbySign(arr)
print("Rearranged Array Elements by Sign:", result)