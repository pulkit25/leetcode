def rob(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    n = len(nums)
    dp = [None] * n
    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2, len(nums)):
        dp[i] = max(dp[:i - 1]) + nums[i]
    return max(dp)