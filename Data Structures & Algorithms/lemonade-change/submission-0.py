class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        coin5 = 0
        coin10 = 0

        if(bills[0]!=5):
            return False

        for i in range(len(bills)):

            if (bills[i] == 5):
                coin5 += 1
            
            elif (bills[i] == 10):
                if(coin5>=1):
                    coin5 -= 1
                else:
                    return False
                coin10 += 1

            else:
                if(coin10>=1 and coin5>=1):
                    coin10 -= 1
                    coin5 -= 1
                elif (coin5 >= 3):
                    coin5 -= 3
                else:
                    return False
        return True
                