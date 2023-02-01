class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        if len(str1) > len(str2):
            max_len = len(str2)
            bigger = str1
            other_str = str2
        else:
            max_len = len(str1)
            bigger = str2
            other_str = str1

        if bigger.startswith(other_str) and bigger.replace(other_str, '') == '':
            return other_str

        for i in range(max_len // 2, -1, -1):
            prefix = other_str[:i]
            if bigger.startswith(prefix):

                if bigger.replace(prefix, '') == '' == other_str.replace(prefix, ''):
                    return prefix
        return ''

"""TEST
Runtime 52 ms
Beats 35.11%
Memory 13.8 MB
Beats 70.81%
"""