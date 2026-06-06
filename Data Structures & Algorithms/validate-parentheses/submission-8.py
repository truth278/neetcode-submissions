class Solution:
    def isValid(self, s: str) -> bool:
        lost = []
        q = ["(", "{", "["]
        for p in s:
            if p in q:
                lost.append(p)
                continue
            if not lost:
                return False
            if p == "}":
                if lost[-1] == "{":
                    lost.pop()
                else:
                    return False
            elif p == ")":
                if lost[-1] == "(":
                    lost.pop()
                else:
                    return False
            else:
                if lost[-1] == "[":
                    lost.pop()
                else:
                    return False     
        return len(lost) == 0