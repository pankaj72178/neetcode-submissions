class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        s = set(nums)
        freq = Counter(nums)
        n = len(nums)
        arr = []
        for i in s:
            if(3*freq[i]>n):
                arr.append(i)
        return arr