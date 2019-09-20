"""
Given an unsorted array of integers, find the maximum contigous subarray sum

"""

def maxContiguousSubarraySum(nums):
    n = len(nums)
    sumSoFar = nums[0]
    currentMax = nums[0]
    for i in range(1, n):
        currentMax = max(nums[i], nums[i]+ currentMax) 
        sumSoFar = max(sumSoFar, currentMax)      
    return sumSoFar

print(maxContiguousSubarraySum( [-2, -3, 4, -1, -2, 1, 5, -3] ))