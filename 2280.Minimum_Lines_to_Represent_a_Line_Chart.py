from decimal import Decimal
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        grad = None
        lines = 0
        stockPrices = sorted(stockPrices, key=lambda x: x[0])
        for i in range(len(stockPrices) - 1):
            cur_grad = Decimal(stockPrices[i][1] - stockPrices[i+1][1]) / Decimal(stockPrices[i][0] - stockPrices[i+1][0])
            if grad != cur_grad:
                lines += 1
                grad = cur_grad
        return lines
