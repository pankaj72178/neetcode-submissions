class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def ispalindrome(word):
            low = 0
            high = len(word) - 1

            while low < high:
                if word[low] != word[high]:
                    return False
                low += 1
                high -= 1

            return True

        result = []

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if ispalindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result