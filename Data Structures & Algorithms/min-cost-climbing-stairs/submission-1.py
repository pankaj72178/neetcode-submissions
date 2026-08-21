class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        arr = [0]*n

        if n==2:
            return min(cost[0],cost[1])
        arr[0] = cost[0]
        arr[1] = cost[1]

        for i in range(n):
            arr[i] = cost[i] + min(arr[i-1],arr[i-2])
        
        return min(arr[-1],arr[-2])