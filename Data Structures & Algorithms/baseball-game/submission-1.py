class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lost=[]
        for l in operations:
            if l=="+":
                lost.append(lost[-1]+lost[-2])
            elif l=="D":
                lost.append(2*lost[-1])
            elif l=="C":
                lost.pop()
            else:
                lost.append(int(l))
        return sum(lost)
