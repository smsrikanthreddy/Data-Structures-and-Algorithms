class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def divide_conquer(low, high, nums, target):
            mid = int(low+high)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                divide_conquer(mid+1, high, nums, target)
            elif nums[mid] > target:
                divide_conquer(low, mid-1, nums, target)
            return mid+1
        return divide_conquer(0, len(nums)-1, nums, target)


class Solution:

    def searchInsert(self, nums, T):
        def search(nums, T, L, R):
            if L > R:
                return L
            mid = (L + R) >> 1
            if nums[mid] == T:
                return mid
            return search(nums, T, mid + 1, R) if nums[mid] < T else search(nums, T, L, mid - 1)
            # if nums[mid]< T:
            #     search(nums, T, mid + 1, R)
            # elif nums[mid]>T:
            #     search(nums, T, L, mid - 1)
            # return mid+1
        return search(nums, T, 0, len(nums)-1)
