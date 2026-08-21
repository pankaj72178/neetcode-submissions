class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for i,num in enumerate(numbers):
            remain = target-num
            if remain in s:
                return [s[remain]+1,i+1]
            s[num] = i