def majorityElement(nums):
    seen = {}
    n = len(nums)
    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
        if seen[num] > n / 2:
            return num
nums = list(map(int, input("Enter array elements: ").split()))
result = majorityElement(nums)
print("Majority Element:", result)