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
    
    def isSubsequenceOptimized(self, sub: str, string: str) -> bool:
        i, j = 0, 0

        while i < len(sub) and j < len(string):
            if sub[i] == string[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return i == len(sub)


obj = Solution()
str1 = 'parent'
sub_str1 = 'are'
notsub_str1 = 'aer'
print(obj.isSubsequenceOptimized(notsub_str1, str1))