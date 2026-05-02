class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=i+1
        while j<len(nums):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i=i+1
                j=j+1
                continue
            j=j+1
        return i+1
        