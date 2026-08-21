class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            x = stones[-1]
            y = stones[-2]

            if (x == y):
                stones.pop()
                stones.pop()
            
            elif (x > y):
                stones.pop(len(stones) - 2)
                stones[-1] = x - y
            
            else:
                stones.pop()
                stones[-1] = y - x
        if len(stones)==0:
            return 0
        return stones[0]