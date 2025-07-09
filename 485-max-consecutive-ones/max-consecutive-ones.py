class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        res=0
        max_ele=0

        for i in nums:
            if i==1:
                count+=1
                max_ele=max(count,max_ele)
            else:
                count=0
        return max_ele
        