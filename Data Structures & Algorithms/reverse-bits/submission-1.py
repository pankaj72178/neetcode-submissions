class Solution:
    def reverseBits(self, n: int) -> int:

        ans = 0

        for _ in range(32):

            ans <<= 1          # Make room for next bit
            ans |= (n & 1)     # Copy last bit of n
            n >>= 1            # Remove last bit

        return ans