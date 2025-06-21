class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmin,curmax=1,1
        for n in nums:
            if n==0:
                curmin,curmax=1,1
                continue
            temp=curmax*n
            temp1=curmin*n
            curmax=max(temp,temp1,n)
            curmin=min(temp,temp1,n)
            res=max(res,curmax)
        return res
        