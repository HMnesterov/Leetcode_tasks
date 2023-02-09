class Nigger:
    def __new__(cls):
        print('1')
        return super().__new__(cls)

    def __init__(self):
        print('2')

    def __call__(self, *args, **kwargs):
        print('3')

s = Nigger()
