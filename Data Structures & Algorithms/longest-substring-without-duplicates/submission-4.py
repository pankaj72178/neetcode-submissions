class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        arr = [0] * 256
        left = 0

        for i in range(len(s)):
            arr[ord(s[i])] += 1

            while arr[ord(s[i])] > 1:
                arr[ord(s[left])] -= 1
                left += 1

            ans = max(ans, i - left + 1)

        return ans