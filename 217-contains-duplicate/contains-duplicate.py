from collections import Counter
class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        for key,value in freq.items():
            if value>1:
                return True
        return False
        
            
        