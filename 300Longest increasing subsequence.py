## 300Longest Increasing Subsequences
"""
solution1:
Use an array result[i] to store the length of longest increasing subsequence
of numbers until index i.
So then when we have number i, we can comare num[i] to each previous number
If nums[i] > nums[j] (0<=j<i), then we can update result[i] as max(result[i], result[j] + 1)
This is O(n^2).
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2: return length
        result = [1] * length
        maxLength = 1
        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    result[i] = max(result[i], result[j] + 1)
            maxLength = max(result[i], maxLength) 
        return maxLength
                
        
"""
solution2: This solution is O(nlogn). It uses a pattern that,
even though we replace one of the number in the longest increasing
subsequences, the total length of the subsequences won't change!!!
We try to keep each number in LIS as small as possible.
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binarySearch(l, start, end, target):
            while start <= end:
                mid = start + (end - start)/2
                if l[mid] == target: return mid
                if l[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return start
        
        length = len(nums)
        if length < 1: return 0
        result = [nums[0]]
        for i in range(1, length):
            if nums[i] > result[-1]:
                result.append(nums[i])
            else:
                pos = binarySearch(result, 0, len(result) - 1, nums[i])
                result[pos] = nums[i]
        return len(result)
                
        
