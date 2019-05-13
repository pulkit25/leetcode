def countBits(self, num: int) -> List[int]:
	num_zeros = []
	num_zeros.append(0)
	for n in range(1, num + 1):
		count = 0
		while n != 0:
			n &= (n - 1)
			count += 1
		num_zeros.append(count)
	return num_zeros