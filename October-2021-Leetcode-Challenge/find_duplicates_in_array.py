class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = {}
        for val in nums:
            output[val] = output.get(val, 0) + 1
        return sorted([k for (k, v) in output.items() if v == 2])
