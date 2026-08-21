class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []

        n1 = len(a)
        n2 = len(b)
        i,j = n1-1,n2-1

        carry = 0

        while i>=0 and j>=0:
            t1 = int(a[i])
            t2 = int(b[j])

            s = t1 + t2 + carry
            carry = s//2

            ans.append(s%2)
            i -= 1
            j -= 1
        
        while i>=0:
            t1 = int(a[i])
            s = t1 + carry
            carry = s//2
            ans.append(s%2)
            i -= 1
        
        while j>=0:
            t2 = int(b[j])
            s = t2 + carry
            carry = s//2
            ans.append(s%2)
            j -= 1
        
        if(carry):
            ans.append(carry)
        k = ''.join(map(str, ans[::-1]))
        return k