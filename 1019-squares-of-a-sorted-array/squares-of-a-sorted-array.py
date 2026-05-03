class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1=[]
        nums2=[]
        i=0
        j=0
        res=[]

        for k in range(0,len(nums)):
            if nums[k]<0:
                nums1.append(nums[k]**2)
            else:
                nums2.append(nums[k]**2)
        nums1.reverse()
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i=i+1
            else:
                res.append(nums2[j])
                j=j+1
        while j<len(nums2):
            res.append(nums2[j])
            j=j+1
        while i<len(nums1):
            res.append(nums1[i])
            i=i+1
        return res




        