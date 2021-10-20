class Solution:
    def reverseWords(self, s: str) -> str:
        # result = []
        # out = s.strip().split(" ")
        # for idx in range(len(out)-1, -1, -1):
        #     if len(out[idx]) > 0:
        #         result.append(out[idx])
        # return " ".join(w for w in result)

        # return ' '.join(reversed(s.split()))

        # joins each word in reversed list placing a space inbetween
        return (' ').join(list(map(str, s.split()))[::-1])


s = "  hello world  "
s = "a good   example"
ins = Solution()
print(ins.reverseWords(s))
