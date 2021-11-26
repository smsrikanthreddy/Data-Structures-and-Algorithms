class Solution:
    ## TC - O(N)
    ## SC - O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_so_far = nums[0]
        max_val = 0
        max_append = []
        for val in nums:
            max_val = max_val + val
            if max_so_far < max_val:
                max_so_far = max_val
            if max_val < 0:
                max_val = 0

        return max_so_far

        ## Method - 2
        ## DP - O(N), O(N)
        def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_max = 0
        for i in range(0, len(nums)):
            curr_max = max(nums[i], curr_max+nums[i])
            max_so_far = max(curr_max, max_so_far)
        return max_so_far
