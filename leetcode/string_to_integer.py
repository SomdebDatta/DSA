class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        ans = 0
        sign = "+"
        index = 0
        if s[index] == "+" or s[index] == "-":
            sign = s[index]
            index += 1
        while index < len(s) and s[index].isdigit():
            ans = ans * 10 + int(s[index])
            index += 1
            if ans.bit_length() >= 32:
                if sign == "-":
                    ans = -2147483648
                else:
                    ans = 2147483647
        return ans

    def myAtoiRec(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        ans = 0
        sign = "+"
        index = 0
        if s[index] == "+" or s[index] == "-":
            sign = s[index]
            index += 1

        def recAtoi(index, ans):
            if index == len(s):
                return int(sign + str(ans))
            if s[index].isdigit():
                ans = ans * 10 + int(s[index])
                index += 1
                if ans.bit_length() >= 32:
                    if sign == "-":
                        return -2147483648
                    return 2147483647
            else:
                return int(sign + str(ans))
            return recAtoi(index, ans)

        return recAtoi(index, ans)


obj = Solution()
print(obj.myAtoiRec("2147483648"))
