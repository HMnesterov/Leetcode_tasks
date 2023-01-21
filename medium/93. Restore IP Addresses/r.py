from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        len_s = len(s)
        variants = set()

        def dfs(new_string, remain_string, remain_count, string_len):
            nonlocal len_s
            if remain_count == 0 and string_len == len_s:
                variants.add(new_string[:-1])
                return
            for i in range(1, len(remain_string) + 1):
                new_part = remain_string[:i]

                if not new_part:
                    continue
                if new_part[0] == '0' and len(new_part) > 1:
                    continue

                if 0 <= int(new_part) <= 255:
                    dfs(new_string + new_part + '.', remain_string[i:], remain_count - 1, string_len + len(new_part))

        dfs('', s, 4, 0)
        return variants


"""TESTS:
1)Runtime 69 ms
Beats 29.64%
Memory 13.9 MB
Beats 79.81%
2)
Runtime 53 ms
Beats 48.26%
Memory 14 MB
Beats 31.50%
"""
