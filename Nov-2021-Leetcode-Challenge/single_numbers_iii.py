class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict_val = {}
        result1 = []
        result2 = []
        for val in nums:
            dict_val[val] = dict_val.get(val, 0) + 1
            if dict_val[val] > 1:
                result1.append(val)
            else:
                result2.append(val)
        return set(result2)-set(result1)


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict_val = {}
        result1 = []
        result2 = []
        for val in nums:
            dict_val[val] = dict_val.get(val, 0) + 1
        return [k for k, v in sorted(dict_val.items(), key=lambda item: item[1])][:2]
