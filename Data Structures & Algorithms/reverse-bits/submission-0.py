class Solution:
    def reverseBits(self, n: int) -> int:

        arr = []
        for _ in range(32):
            arr.append(n & 1)
            n >>= 1

        ans = 0

        for i in range(32):
            ans += arr[i] * (1 << (31 - i))

        return ans