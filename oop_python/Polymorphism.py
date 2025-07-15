def basic_polymorhpism():
    class Number:
        def __init__(self, val):
            self.val = val

        def __add__(self, obj):
            """Overriding the '+' method"""
            return self.val + obj.val
        
        def __gt__(self, obj):
            """Overriding the '>' method"""
            if self.val > obj.val:
                return True
            return False
        
        def __str__(self):
            return f'This is an object of class Number with value {self.val}'
    
    n1 = Number(5)
    n2 = Number(10)
    print(n1 + n2)
    print(n1 > n2)
    print(n2 > n1)
    print(n1)

if __name__ == '__main__':
    basic_polymorhpism()