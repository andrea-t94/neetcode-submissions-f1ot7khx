class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first BS to find pivot idx
        l, r = 0, len(nums)-1

        # pivot is first num lower then nums[r]
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        # BS on one of the halves only
        l, r = 0, len(nums)-1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        
