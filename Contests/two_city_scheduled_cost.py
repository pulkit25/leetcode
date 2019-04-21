def twoCitySchedCost(self, costs: List[List[int]]) -> int:
	cost = 0
	def sorting_func(x):
		return abs(x[0] - x[1])
	costs.sort(key = sorting_func, reverse = True)
	a = len(costs) // 2
	b = len(costs) - a
	while len(costs) > 0:
		if costs[0][0] < costs[0][1]:
			if a > 0:
				cost += costs[0][0]
				costs.remove(costs[0])
				a -= 1
			else:
				cost += costs[0][1]
				costs.remove(costs[0])
				b -= 1                    
		else:
			if b > 0:
				cost += costs[0][1]
				costs.remove(costs[0])
				b -= 1
			else:
				cost += costs[0][0]
				costs.remove(costs[0])
				a -= 1
	return cost