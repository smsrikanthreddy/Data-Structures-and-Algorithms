class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 0
        while idx < n-1:
            if nums[idx] == nums[idx+1]:
                idx += 2
            else:
                return nums[idx]
        return nums[idx]
