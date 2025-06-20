class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]    0

        comp={}
        for i in range(len(nums)):
            if nums[i] in comp:
                return [i,comp[nums[i]]]
            else:
                comp[target-nums[i]]=i