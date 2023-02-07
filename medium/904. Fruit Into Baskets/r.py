from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        values = set()
        hash_table = defaultdict(int)
        elems = []
        elems_count = 0
        second_count = 0
        second_value = None
        for val in fruits:

            if val not in elems and len(elems) >= 2:
                values.add(elems_count)



                elems_count = second_count + 1
                elems.remove(*set(elems) - {second_value})


                elems.append(val)
                hash_table[second_value] = 0
                hash_table[val] = 1

            elif val not in elems:
                elems.append(val)
                elems_count += 1
                hash_table[val] = 1

            else:
                elems_count += 1
                hash_table[val] += 1

            if second_value == val:
                second_count += 1
            else:
                second_value, second_count = val, 1

        else:
            values.add(elems_count)
        return max(values)

"""TESTS:
1)Runtime 819 ms
Beats 96.18%
Memory 20 MB
Beats 90.85%
2)Runtime 807 ms
Beats 97.40%
Memory 20 MB
Beats 80.52%"""