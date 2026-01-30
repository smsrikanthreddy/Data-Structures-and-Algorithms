class Solution:
    def sorting(self, nums: List[int]) -> List[int]:
        # quick sorting
        def swap(nums, arr1, arr2):
            temp = nums[arr1]
            nums[arr1] = nums[arr2]
            nums[arr2] = temp

        def partition(nums, low, high):
            pivot = nums[low]
            i = low
            j = high
            while i < j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i < j:
                    swap(nums, i, j)
            return j

        def quick_sort(nums, low, high):
            if low < high:
                mid = partition(nums, low, high)
                quick_sort(nums, low, mid)
                quick_sort(nums, mid+1, high)
            return nums

        print(quick_sort(nums, 0, len(nums)-1))

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
        # for i in range(1, n):
        #     for j in range(i, 0, -1):
        #         if nums[j-1] > nums[j]:
        #             nums[j-1], nums[j] = nums[j], nums[j-1]
        #
        # return nums
