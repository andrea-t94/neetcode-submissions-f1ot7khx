class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hMap = defaultdict(int)
        for c in s:
            hMap[c] += 1
        
        res = ""
        for c in order:
            if c in hMap:
                res += c*hMap[c]
                del hMap[c]
        
        for c in hMap:
            res += c*hMap[c]
        
        return res

