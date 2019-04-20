def maxProfit(self, prices: List[int]) -> int:
	if len(prices) == 0:
		return 0
	max_profit = 0
	min_element = prices[0]
	for i in range(len(prices)):
		if prices[i] - min_element > max_profit:
			max_profit = prices[i] - min_element
		if prices[i] < min_element:
			min_element = prices[i]
	return max_profit