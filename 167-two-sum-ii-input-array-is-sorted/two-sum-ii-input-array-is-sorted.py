class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i,k in enumerate(numbers):
            diff=target-k
            if diff in seen:
                return seen[diff],i+1

            else:
                seen[k]=i+1
        
     