class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ''' represent each str as arr of 26 chars '''
        res = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c)-ord('a')] += 1
            res[tuple(cnt)].append(s)
        return list(res.values())