class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        # main_res = []
        main_res = {}
        for i in range(n):
            if accounts[i] not in main_res:
                main_res[accounts[i]] = accounts[i+1:]
            else:
                dict_value = main_res[accounts[i]]
                main_res[accounts[i]].update
