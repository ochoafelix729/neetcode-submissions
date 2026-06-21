class StockSpanner:

    def __init__(self):
        self.quotes = []

    def next(self, price: int) -> int:
        self.quotes.append(price)
        top = len(self.quotes) - 1
        span = 0
        while top >= 0 and self.quotes[top] <= price:
            top -= 1
            span += 1
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)