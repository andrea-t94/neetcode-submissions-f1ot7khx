class Solution:
    def compress(self, chars: List[str]) -> int:
        w,l,r = 0,0,0 #w id idx to write, l and r start and end of current char
        n = len(chars)
        
        while r < n:
            chars[w] = chars[l] #firt char has to remain as char
            w += 1 
            # move until find a new char
            while r < n and chars[l] == chars[r]:
                r += 1
            if r-l > 1:
                for num in str(r-l):
                    chars[w] = num
                    w += 1
            l = r  
        return w
            