class StockSpanner:

    def __init__(self):
        self.stockSpanner = []

    def next(self, price: int) -> int:
        self.stockSpanner.append(price)

        ans = 0
        i = len(self.stockSpanner) - 1
        while i >=0 and self.stockSpanner[i] <= price:
            ans += 1
            i -= 1
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)