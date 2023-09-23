class Solution:
    def intToRoman(self, num: int) -> str:
        subtraction_map = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        placing_map = {1: ["I", "V"], 2: ["X", "L"], 3: ["C", "D"], 4: ["M"]}
        roman = ""

        reverse_num_list = list(str(num)[::-1])

        for i in range(len(reverse_num_list)):
            digit = int(reverse_num_list[i]) * (10**i)
            if digit in subtraction_map.keys():
                roman = subtraction_map[digit] + roman
                continue
            if digit > 0 and digit < 10:
                if digit < 4:
                    roman = (placing_map[1][0] * digit) + roman
                else:
                    roman = (
                        placing_map[1][1] + (placing_map[1][0] * (digit - 5))
                    ) + roman
            elif digit < 100:
                if digit in (40, 90):
                    roman = subtraction_map.get(digit) + roman
                elif digit < 40:
                    roman = (placing_map[2][0] * (digit // 10)) + roman
                else:
                    roman = (
                        placing_map[2][1] + (placing_map[2][0] * ((digit - 50) // 10))
                    ) + roman
            elif digit < 1000:
                if digit in (400, 900):
                    roman = subtraction_map.get(digit) + roman
                elif digit < 400:
                    roman = (placing_map[3][0] * (digit // 100)) + roman
                else:
                    roman = (
                        placing_map[3][1] + (placing_map[3][0] * ((digit - 500) // 100))
                    ) + roman
            else:
                roman = ((placing_map[4][0] * (digit // 1000))) + roman
        return roman

    def soln(self, num: int) -> str:
        roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        romanized = ""

        for base, symb in roman.items():
            romanized += symb * (num // base)
            num %= base
        else:
            return romanized


inp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 49, 99, 862, 999, 1234]
inp_list2 = [80, 81, 84, 89]
inp_list_sub = [4, 9, 49]
obj = Solution()
# for integer in inp_list:
print(obj.soln(1234))
