class Solution(object):
    def longestSubarray(self, nums):
        m = max(nums)  
        counter = 0    
        longest = 0   
        
        for num in nums:
            if num == m:
                counter += 1 
            else:
                longest = max(longest, counter)  
                counter = 0  
        
        longest = max(longest, counter)  
        return longest  


