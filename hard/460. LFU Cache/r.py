from collections import OrderedDict


class LFUCache:
    def _update_ordered_dict(self, key, value, new_count):
        if new_count not in self.hash_ordered:
            self.hash_ordered[new_count] = OrderedDict()
        self.hash_ordered[new_count][key] = value
        self.hash_ordered[new_count].move_to_end(key)

    def __init__(self, capacity: int):
        self.hash_table = {}
        self.hash_ordered = {}
        self.capacity = capacity
        self.min_count = 0
        self.used = 0

    def get(self, key: int) -> int:
        val = -1
        if key in self.hash_table:
            val = self.hash_table[key][0]
            old_count = self.hash_table[key][1]
            self.hash_table[key][1] += 1
            del self.hash_ordered[old_count][key]
            new_count = old_count + 1

            self._update_ordered_dict(key, val, new_count)

            if self.min_count == old_count and len(self.hash_ordered[old_count]) == 0:
                self.min_count = new_count
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.hash_table:
            self.hash_table[key][0] = value
            old_count = self.hash_table[key][1]
            self.hash_table[key][1] += 1
            del self.hash_ordered[old_count][key]
            new_count = old_count + 1

            self._update_ordered_dict(key, value, new_count)

            if self.min_count == old_count and len(self.hash_ordered[old_count]) == 0:
                self.min_count = new_count



        else:
            if self.used < self.capacity:
                self.hash_table[key] = [value, 1]
                self._update_ordered_dict(key, value, 1)
                self.used += 1
                self.min_count = 1

            else:
                del_key, del_value = self.hash_ordered[self.min_count].popitem(0)
                del self.hash_table[del_key]

                self.hash_table[key] = [value, 1]
                self._update_ordered_dict(key, value, 1)
                self.min_count = 1

"""TESTS
1) Runtime  817 ms
Beats  89.30%
Memory  78.9 MB
Beats  31.99%"""