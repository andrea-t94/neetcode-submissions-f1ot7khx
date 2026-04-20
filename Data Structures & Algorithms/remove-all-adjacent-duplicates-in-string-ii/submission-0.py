class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ''' use a stack to keep track of char and count of adjacent duplicates
        once cnt == k, start popping '''

        stack = [] # [char, cnt]
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
            if stack[-1][1] == k:
                stack.pop()
        
        return ''.join(char*cnt for char, cnt in stack)

        