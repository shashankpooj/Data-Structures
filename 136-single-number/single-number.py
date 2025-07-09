from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        freq=Counter(nums)
        for key,value in freq.items():
            if value==1:
                res=key
        return res
                
        
        