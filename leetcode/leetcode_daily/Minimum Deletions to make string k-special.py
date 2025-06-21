from collections import defaultdict
from math import inf


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        char_map = defaultdict(int)
        for letter in word:
            char_map[letter] += 1

        res = inf

        for letter1 in char_map:
            deleted = 0
            for letter2 in char_map:
                if char_map[letter2] < char_map[letter1]:
                    deleted += char_map[letter2]
                elif char_map[letter2] - char_map[letter1] - k > 0:
                    deleted += char_map[letter2] - char_map[letter1] - k
            res = min(res, deleted)
        return res


obj = Solution()
word = "dabdcbdcdcd"
k = 2
print(obj.minimumDeletions(word, k))
