
def inheritance_mro():
    """
    This function explains the Method Resolution Order (MRO) in python.
    If there is multiple inheritance, then the methods (including init and other methods) are resolved
    left to right.
    In the below example, C inherits from A and B
    """
    class A:
        def __init__(self):
            print('Inside A\'s init')

        def feature1(self):
            print('feature1-A working...')
        
    class B:
        def __init__(self):
            print('Inside B\'s init')
        
        def feature1(self):
            print('feature1-B working...')

        def feature2(self):
            print('feature2-B working')

    class C(A,B):
        def __init__(self):
            super().__init__()
            print('Inside C\'s init')
        
        def feature1(self):
            print('feature1-C working...')

        def feature3(self):
            print('Feature3-C working')
        
        def feat(self):
            super().feature1()

    c = C()
    c.feature1()
    c.feat()

if __name__ == '__main__':
    inheritance_mro()
