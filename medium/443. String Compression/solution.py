from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        last_char = None
        count = 0
        new_l = []
        for indx, i in enumerate(chars):
            if not last_char:
                last_char = i
                count = 1
            elif i == last_char:
                count += 1
            else:
                if count == 1:
                    new_l.append(last_char)
                else:
                    new_l.extend([last_char] + list(str(count)))

                last_char = i
                count = 1
        if count == 1:
            new_l.append(last_char)
        else:
            new_l.extend([last_char] + list(str(count)))

        chars.extend(new_l)
        del chars[:indx + 1]

"""TESTS
1)
Runtime 53 ms
Beats 95.94%
Memory 13.9 MB
Beats 65.1%
2)Runtime 61 ms
Beats 68.22%
Memory 14.1 MB
Beats 25.81%
"""

