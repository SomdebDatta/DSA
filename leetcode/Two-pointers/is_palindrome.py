class Solution:

    def isPalindrome(self, s: str) -> bool:
        ct = 0
        palindrome = True
        s_length = len(s)
        first, last = 0, s_length-1
        while ct < (s_length // 2) and last >= 0 and first < s_length:
            if not s[first].lower().isalnum():
                first += 1
            elif not s[last].lower().isalnum():
                last -= 1
            elif s[first].lower() != s[last].lower():
                return False
            else:
                first += 1
                last -= 1
                ct += 1
        return palindrome


obj = Solution()
# print(obj.isPalindrome('helloolleh'))
# print(obj.isPalindrome(' '))
# print(obj.isPalindrome('a.b,.'))
print(obj.isPalindrome(',.'))




