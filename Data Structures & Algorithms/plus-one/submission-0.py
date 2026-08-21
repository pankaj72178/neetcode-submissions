class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        ans = []
        carry = 1
        
        for i in range(len(digits)-1 , -1 , -1):
            num = digits[i] + carry

            carry = num // 10
            ans.append(num%10)
            
        if carry:
            ans.append(carry)
        
        ans = ans[::-1]
        return ans