class Solution:
    def nextGreaterElement(self, nums1, nums2):

        m, n = len(nums1), len(nums2)
        result = [-1]*m

        for idx1 in range(m):
            flag = False
            for idx2 in range(n):
                if flag is False and nums2[idx2] == nums1[idx1]:
                    flag = True
                    if idx2+1 == n:
                        break
                if flag is True:
                    if nums1[idx1] < nums2[idx2]:
                        result[idx1] = nums2[idx2]
                        break
        return result


ins = Solution()
lst1 = [4, 1, 2]
lst2 = [1, 3, 4, 2]
lst1 = [4, 1, 2]
lst2 = [1, 2, 3, 4]
print(ins.nextGreaterElement(lst1, lst2))
