class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        targetSum = sum(nums)
        if targetSum%k != 0:
            return False
        
        target = targetSum/k
        n = len(nums)
        used = [False] * n
        def dfs(i, k, curSum):
            if k == 0:
                return True
            if curSum == target:
                return dfs(0, k-1, 0)
            for i in range(i, n):
                if used[i] or curSum+nums[i] > target:
                    continue
                used[i] = True
                if dfs(i+1, k, curSum+nums[i]):
                    return True
                used[i] = False
            return False
        
        return dfs(0,k,0)
            