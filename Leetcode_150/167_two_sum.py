#1Two Pointer :- 67. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start < end:
            if numbers[start]+numbers[end] == target:
                return [start+1, end+1]
            elif numbers[start]+numbers[end] > target:
                end -= 1
            else:
                start += 1
        return [start+1, end+1]
    
#TC :-  O(N)
#SC :-O(1)