class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recPow(x=x, n=n):
            if n == 0:
                return 1
            if n % 2 == 0:
                return recPow(x * x, n // 2)
            else:
                return x * recPow(x * x, (n - 1) // 2)

        ans = recPow()

        return float(ans) if n >= 0 else 1 / ans


obj = Solution()
print(obj.myPow(0.99999, 948688))
