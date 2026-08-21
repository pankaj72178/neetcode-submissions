class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        ans = 0

        for i in range(32):
            bit = (left >> i) & 1
            if not bit:
                continue
            
            remain = left % (1<<(i+1))
            diff = (1<<(i+1)) - remain

            if (right - left < diff):
                ans = ans | (1<<i)

        return ans