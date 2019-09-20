"""
Given an unsorted array of integers, find the number of subarrays having sum exactly equal to a given number k.

Examples:

Input : arr[] = {10, 2, -2, -20, 10}, 
        k = -10
Output : 3
Subarrays: arr[0...3], arr[1...4], arr[3..4]
have sum exactly equal to -10.

Input : arr[] = {9, 4, 20, 3, 10, 5},
            k = 33
Output : 2
Subarrays : arr[0...2], arr[2...4] have sum
exactly equal to 33.
"""

def findSubarraySub(nums, k): 
    preSum = {}
    preSum[0] = 1
    n = len(nums)
    sum = 0
    res = 0
    for i in range(n): 
        sum += nums[i]
        if sum - k in preSum:
            res += preSum[sum - k]
        if sum in preSum:
            preSum[sum] += 1
        else:
            preSum[sum] = 1
    return res

array = [-1, 1, -1, 1]
k = 0

print(findSubarraySub(array, k))