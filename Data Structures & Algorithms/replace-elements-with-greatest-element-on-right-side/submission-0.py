class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[0]*n
        r=-1
        for i in range(n-1,-1,-1):
            ans[i]=r
            r=max(r,arr[i])
        return ans