from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_count = 0
        res = 0
        for key, value in freq.items():
            if value > max_count:
                max_count = value
                res = key
        return res
        