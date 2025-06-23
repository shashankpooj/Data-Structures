class Solution:
    def hammingWeight(self, n: int) -> int:
        # count=0
        # while n>0:
        #     n=n%2
        #     if n==1:
        #         count=count+1
        #     n=n//10
        # return count
        
    
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n // 2  # divide by 2 to shift bits
        return count


        