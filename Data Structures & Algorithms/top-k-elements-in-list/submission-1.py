class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sorting on the array of freq
        # possible bc we have a cap on the val that can have
        hMap = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            hMap[num] += 1
        for num,cnt in hMap.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
