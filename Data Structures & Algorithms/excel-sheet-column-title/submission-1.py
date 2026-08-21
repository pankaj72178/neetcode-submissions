class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        arr = []
        while columnNumber:

            columnNumber -= 1

            rem = columnNumber%26

            arr.append(chr(65+rem))
        
            columnNumber = columnNumber//26

        s = ''.join(arr[::-1])
        return s