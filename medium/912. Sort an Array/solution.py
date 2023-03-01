from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        new_lst = []
        def merge_two_sorted_lists(list1, list2):
            new_lst = []
            indx1, indx2 = 0, 0
            len_l_1, len_l_2 = len(list1), len(list2)
            while len_l_1 > indx1 and len_l_2 > indx2:
                if list1[indx1] < list2[indx2]:
                    new_lst.append(list1[indx1])
                    indx1 += 1
                elif list1[indx1] > list2[indx2]:
                    new_lst.append(list2[indx2])
                    indx2 += 1
                else:
                    new_lst.append(list1[indx1])
                    new_lst.append(list2[indx2])
                    indx1 += 1
                    indx2 += 1
            if indx1 < len_l_1:
                new_lst.extend(list1[indx1:])
            else:
                new_lst.extend(list2[indx2:])
            return new_lst

        def merge_split_and_connect(nums):

            num_len = len(nums)
            if num_len <= 2:
                return sorted(nums)
            split_one = merge_split_and_connect(nums[:num_len // 2])
            split_two = merge_split_and_connect(nums[num_len // 2:])
            return merge_two_sorted_lists(split_one, split_two)

        return merge_split_and_connect(nums)

"""TESTS:
1)Runtime 1616 ms
Beats 74.94%
Memory 23 MB
Beats 31.75%
2)Runtime 1622 ms
Beats 74.69%
Memory 22.8 MB
Beats 39.15%"""