def maxProfit(self, prices: List[int]) -> int:
	if len(prices) == 0:
		return 0
	max_profit = 0
	min_element = prices[0]
	for i in range(len(prices)):
		max_profit = max(max_profit, prices[i] - min_element)
		min_element = min(min_element, prices[i])
	return max_profit