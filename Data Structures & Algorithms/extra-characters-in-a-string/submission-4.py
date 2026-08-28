class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self,words):
        self.root = TrieNode()
        for word in words:
            curr = self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.isEnd = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary).root
        dp = { len(s): 0 }

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i+1)
            curr = trie
            for j in range(i,len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isEnd:
                    res = min(res,dfs(j+1))
            dp[i] = res
            return res
        return dfs(0)