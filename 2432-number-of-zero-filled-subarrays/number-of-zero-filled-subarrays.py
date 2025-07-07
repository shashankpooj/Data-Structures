class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # nums = [1, 3, 0, 0, 2, 0, 0, 4]

    #    nums = [0, 0, 0, 2, 0, 0]

        count = 0        # to track consecutive zeros
        res = 0          # total number of zero-filled subarrays

        for i in nums:
            if i == 0:
                count += 1        # increment zero streak
                res += count      # add all subarrays ending at this zero
            else:
                count = 0   
        return res      # reset if non-zero


