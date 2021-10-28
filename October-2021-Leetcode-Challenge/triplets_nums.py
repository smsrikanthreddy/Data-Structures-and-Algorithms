# To DO


# O(N)^3
# class Solution:
#     def threeSum(self, nums):
#         n = len(nums)
#         if n == "" or n == 1 or n == 2:
#             return []
#         result = []
#
#         for i in range(n-2):
#             for j in range(i+1, n-1):
#                 for k in range(j+1, n):
#                     if i != j and j != k and i != k and nums[i]+nums[j]+nums[k] == 0:
#                         out = [nums[i], nums[j], nums[k]]
#                         # breakpoint()
#                         vals = set(sorted(out))
#                         if len(result) == 0:
#                             result.append(out)
#                         else:
#                             flag = True
#                             for ans_val in result:
#                                 if vals == set(sorted(ans_val)):
#                                     flag = False
#                             if flag is True:
#                                 result.append(out)
#                     else:
#                         continue
#         return result

# O(N)^2 #space O(n)  Improve the solution to better
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == "" or n == 1 or n == 2:
            return []
        Set = set()

        nums.sort()  # nlog(N)

        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                triplet_sum = nums[i]+nums[j]+nums[k]
                if triplet_sum == 0:
                    Set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif triplet_sum < 0:
                    j += 1
                else:
                    k -= 1
        return [list(i) for i in Set]

##
# Better solutions


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # nlogn
        n = len(nums)
        rst = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # just make it faster..not chane the time complexity
                continue

            # use two pointers, since it been sorted
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    rst.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # remove duplication
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    # while nums[r] == nums[r + 1] and l < r: # even not necessary
                    #    r-=1

        return rst


inp = [-1, 0, 1, 2, -1, -4]
ins = Solution()
print(ins.threeSum(inp))
