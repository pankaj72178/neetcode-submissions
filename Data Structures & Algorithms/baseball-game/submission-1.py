class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []

        for ch in operations:

            if ch == "+":
                arr.append(arr[-1] + arr[-2])

            elif ch == "D":
                arr.append(2 * arr[-1])

            elif ch == "C":
                arr.pop()

            else:
                arr.append(int(ch))

        return sum(arr)