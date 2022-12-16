class MyQueue:

    def __init__(self):
        self.lst = []

    def push(self, x: int) -> None:
        return self.lst.append(x)

    def pop(self) -> int:
        return self.lst.pop(0)

    def peek(self) -> int:
        return self.lst[0]

    def empty(self) -> bool:
        return not bool(self.lst)

"""TESTS:
1)Runtime 31 ms
Beats 92.51%
Memory 13.8 MB
Beats 99.94%
2)Runtime 32 ms
Beats 91.33%
Memory 13.9 MB
Beats 76.9%"""