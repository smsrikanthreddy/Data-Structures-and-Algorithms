class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Selection Sort - O(N)^2, O(1)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] > nums[j]:
        #             nums[j], nums[i] = nums[i], nums[j]
        # return nums

        # # Bubble sort O(n)^2, O(1)
        # for i in range(n):
        #     swap = False
        #     for j in range(0, n-i-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #             swap = True
        #     if swap is False:
        #         break

        # insertion sort O(n)^2, O(1)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]

        return nums


A = [2, 0, 2, 1, 1, 0]
ins = Solution()
print(ins.sortColors(A))
