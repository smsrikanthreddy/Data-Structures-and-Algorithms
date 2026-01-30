# Using formula
# TC -
# SC -
class Solution:
    def numTrees(self, n: int) -> int:
        def factorial(n):
            fact = 1
            for val in range(1, n+1):
                fact = fact*val
            return fact

        # countBST  = (2*n)! / ((n + 1)! * n!)
        n_fact = factorial(n)
        denom = (n_fact * (n+1)) * (n_fact)
        n2_fact = factorial(2*n)
        return int(n2_fact/denom)
