class Solution:
    def isSubsequence(self, sub: str, string: str) -> bool:
        curr = 0
        sub_len = len(sub)

        if sub_len == 0:
            return True

        for i in range(len(string)):
            if string[i] == sub[curr]:
                if curr == sub_len-1:
                    return True
                curr += 1
                continue
            else:
                continue
        return False


obj = Solution()
str1 = 'parent'
sub_str1 = 'are'
notsub_str1 = 'aer'
print(obj.isSubsequence('', str1))