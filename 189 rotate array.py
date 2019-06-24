## 189 rotate array
"""
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

solution:
It's similat to "I love Yahoo".
This requires to reverse whole string, then reverse according to the k steps.
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(start, end, l):
            while start < end:
                tmp = l[start]
                l[start] = l[end]
                l[end] = tmp
                start += 1
                end -= 1
                
                #print(l)
            return l
        
        length = len(nums)
        step = length -  k % length
        nums  = swap(0, length -1, nums)
        nums = swap(0, length - step - 1, nums)
        nums = swap(length - step, length - 1, nums)
            
        
