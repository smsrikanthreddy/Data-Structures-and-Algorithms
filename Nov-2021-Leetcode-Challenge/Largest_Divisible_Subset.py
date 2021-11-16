class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
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

        quick_sort(nums, 0, len(nums)-1)

        count_vals = [1]*len(nums)
        actual_vals = count_vals.copy()

        for i in range(len(nums)):
            for j in range(i, -1, -1):
                if nums[i] % nums[j] == 0:
                    actual_vals[i] = max(actual_vals[i], actual_vals[j]+1)
        maxIndex = 0
        for v in range(0, len(nums)):
            if actual_vals[v] > actual_vals[maxIndex]:
                maxIndex = v
        result = []
        temp = nums[maxIndex]
        current = actual_vals[maxIndex]
        for k in range(maxIndex, -1, -1):
            if (temp % nums[k] == 0) and (current == actual_vals[k]):
                result.append(nums[k])
                temp = nums[k]
                current -= 1
        return result
