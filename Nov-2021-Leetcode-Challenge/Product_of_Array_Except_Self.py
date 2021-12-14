class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            sum_val = 1
            for val in nums[:i]+nums[i+1:]:
                sum_val *= val
            res.append(sum_val)
        return res

    # Method 2
    def productExceptSelf(self, nums):
        pre, suf, n = list(accumulate(nums, mul)), list(
            accumulate(nums[::-1], mul))[::-1], len(nums)
        return [(pre[i-1] if i else 1) * (suf[i+1] if i+1 < n else 1) for i in range(n)]

    # Method 3
    def productExceptSelf(self, nums):
        prod, zero_cnt = reduce(lambda a, b: a*(b if b else 1), nums, 1), nums.count(0)
        if zero_cnt > 1:
            return [0]*len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                nums[i] = 0 if c else prod
            else:
                nums[i] = prod // c
        return nums


res_val = Solution()
nums = [1, 2, 3, 4]
print(res_val.productExceptSelf(nums))
