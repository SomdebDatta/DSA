class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n % 2 == 0:
            ans = (5 ** (n / 2)) * (4 ** (n / 2)) % 1000000007
        else:
            ans = (5 ** ((n + 1) / 2)) * (4 ** ((n - 1) / 2)) % 1000000007

        return int(ans)


obj = Solution()
print(obj.countGoodNumbers(50))
