class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       seen={}
       for i,nums in enumerate(numbers):
            diff=target-nums
            if diff in seen:
                return seen[diff],i+1
            else:
                seen[nums]=i+1
        
     