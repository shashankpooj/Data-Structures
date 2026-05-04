class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=i+1
        n=len(nums)-1
        while j<=n:
            if nums[i]!=nums[j]:
                i=i+1
                
                nums[i]=nums[j]
                j=j+1
                # continue
            else:
                j=j+1
        return i+1
        