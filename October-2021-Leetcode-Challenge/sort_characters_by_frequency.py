class Solution:
    def frequencySort(self, s: str) -> str:
        dict_val = {}
        for val in s:
            dict_val[val] = dict_val.get(val, 0) + 1
        rev_list = sorted(dict_val, key=dict_val.get, reverse=True)
        s_r = ""
        for wv in rev_list:
            repeats = [wv] * dict_val[wv]
            s_r = s_r+"".join(repeats)
        return s_r
