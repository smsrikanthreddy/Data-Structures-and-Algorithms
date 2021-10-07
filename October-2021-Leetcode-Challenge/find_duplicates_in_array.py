# O(N), O(N) - extra array is used
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = {}
        for val in nums:
            output[val] = output.get(val, 0) + 1
        return sorted([k for (k, v) in output.items() if v == 2])

## O(N), O(1)


def printRepeating(arr, size):

    print("The repeating elements are: ")

    for i in range(0, size):

        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")


# Driver code
arr = [1, 2, 3, 1, 3, 6, 6]
arr_size = len(arr)

printRepeating(arr, arr_size)
