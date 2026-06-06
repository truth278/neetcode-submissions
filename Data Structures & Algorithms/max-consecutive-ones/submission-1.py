class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=mox=0
        for num in nums:
            if num:
                count+=1
            else: 
                count=0
            mox=max(mox,count)
        return mox    

