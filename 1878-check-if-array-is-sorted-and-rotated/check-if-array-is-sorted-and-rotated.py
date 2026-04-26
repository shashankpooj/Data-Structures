class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        last=nums[len(nums)-1]
        first=nums[0]
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
        if last>first:
            count+=1
        if count>1:
            return False
        return True
        
               
             
            
        