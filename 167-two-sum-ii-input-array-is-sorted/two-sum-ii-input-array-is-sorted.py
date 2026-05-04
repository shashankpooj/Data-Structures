class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
           
        for index,value in enumerate(numbers):
            diff=target-value
            if diff in seen:
                return seen[diff],index+1
            else:
                seen[value]=index+1