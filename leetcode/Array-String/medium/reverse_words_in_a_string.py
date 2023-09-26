class Solution:
    def reverseWords(self, s: str) -> str:
        ongoing_word = False
        start_word_index = 0
        ans_list = list()
        for i in range(len(s)):
            if ongoing_word:
                if s[i] == " ":
                    ans_list.append(s[start_word_index:i])
                    ongoing_word = False
                else:
                    if i == len(s) - 1:
                        ans_list.append(s[start_word_index : i + 1])
                        break
                    continue
            else:
                if s[i] == " ":
                    continue
                else:
                    if i == len(s) - 1:
                        ans_list.append(s[i::])
                        break
                    start_word_index = i
                    ongoing_word = True

        return " ".join(ans_list[::-1])


inp = " hello i am somdeb"
inp = " asdasd df f"
obj = Solution()
print(obj.reverseWords(inp))
