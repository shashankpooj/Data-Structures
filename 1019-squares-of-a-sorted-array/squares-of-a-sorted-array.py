class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1=[]
        arr2=[]
        for i in range(len(nums)):
            if nums[i]<=0:
                arr1.append(nums[i]**2)
            else:
                arr2.append(nums[i]**2)
        arr1.reverse()
        n1=len(arr1)
        n2=len(arr2)
        i=0
        j=0
        res=[]
        while i<n1 and j<n2:
            if arr1[i]<arr2[j]:
                res.append(arr1[i])
                i=i+1
            else:
                res.append(arr2[j])
                j=j+1
        while i<n1:
            res.append(arr1[i])
            i=i+1
        while j<n2:
            res.append(arr2[j])
            j=j+1
        return res
        


        





        