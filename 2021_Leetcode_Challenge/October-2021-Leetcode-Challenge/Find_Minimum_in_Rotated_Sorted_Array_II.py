class Solution:
    def findMin(self, nums: List[int]) -> int:
        # solution 1
        # return min(nums)

        # solution 2
        left = 0
        right = len(nums)-1

        while left < right:
            mid = int((left + right)/2)
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] == nums[right]:
                right = right - 1
            else:
                left = mid+1
        return nums[left]
