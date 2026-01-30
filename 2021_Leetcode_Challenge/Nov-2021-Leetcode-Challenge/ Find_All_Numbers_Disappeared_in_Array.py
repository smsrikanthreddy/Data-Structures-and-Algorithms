class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Method 1
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # return set(range(1, len(nums)+1)) - set(nums)

        # Method 2
        # TC - O(N^2)
        # SC  - O(1)
        # return [val for val in range(1, len(nums)+1) if val not in nums]

        # Method 3
        # TC - O(N)
        # SC  - O(N)
        # hashlist
        s = Counter(nums)
        return [i for i in range(1, len(nums)+1) if i not in s]

        # Method 4
        ans = []
        seen = [False]*(len(nums)+1)
        for c in nums:
            seen[c] = True
        for i in range(1, len(nums)+1):
            if not seen[i]:
                ans.append(i)
        return ans

        # Method 4
        # TC - O(N^2)
        # SC  - O(1)
        nums.sort()
        for val in range(1, len(nums)):
            binary_search
         return [val for val in range(1, len(nums)+1) if val not in nums]
