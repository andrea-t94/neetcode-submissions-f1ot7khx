class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(perm, nums, used):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                perm.append(nums[i])
                dfs(perm, nums, used)
                perm.pop()
                used[i] = False
        
        res = []
        dfs([], nums, [False]*len(nums))
        return res
            