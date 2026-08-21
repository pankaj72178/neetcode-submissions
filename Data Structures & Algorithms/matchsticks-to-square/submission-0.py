class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks)<4:
            return False
        
        if len(matchsticks)==4:
            for i in range(1,4):
                if(matchsticks[i]!=matchsticks[i-1]):
                    return False
            return True
        
        sm = sum(matchsticks)
        mx = max(matchsticks)

        if( sm%4 != 0):
            return False

        if( 4*mx > sm):
            return False
        
        t = sm//4

        matchsticks.sort(reverse=True)

        sides = [0] * 4

        def backtrack(index):
            if index == len(matchsticks):
                return all(side == t for side in sides)

            for i in range(4):
                if sides[i] + matchsticks[index] <= t:
                    sides[i] += matchsticks[index]

                    if backtrack(index + 1):
                        return True

                    sides[i] -= matchsticks[index]

                # Optimization
                if sides[i] == 0:
                    break

            return False

        return backtrack(0)