class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
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
             # return nums

        data = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                data.append(mat[i][j])
        print(data)
        quick_sort(data, 0, len(nums)-1)
