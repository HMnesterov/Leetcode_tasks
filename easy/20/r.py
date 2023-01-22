def func(s):
    s = " "

    string = ''

    for i in s:
        if i.isalpha():
            string += i.lower()
            continue
        if i.isdigit():
            string += i
    return string

"""TESTS:
1)Runtime 35 ms
Beats 99.64%
Memory 13.9 MB
Beats 79.81%
2)
Runtime 56 ms
Beats 42.26%
Memory 14 MB
Beats 31.50%
"""
