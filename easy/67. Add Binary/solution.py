class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0':
            return b
        if b == '0':
            return a
        def convert_to_10(digit):

            new_digit = 0
            for indx, value in enumerate(digit[::-1]):
                new_digit += int(value) * 2 ** indx

            return new_digit

        def convert_to_2(digit):
            new_str = ''
            while digit:
                new_str += str(digit % 2)
                digit //= 2

            return new_str[::-1]

        new_digit = convert_to_10(a) + convert_to_10(b)

        return convert_to_2(new_digit)

"""TESTS
1) Runtime 39 ms Beats 48.9% Memory 13.9 MB Beats 63.5%
2)"""