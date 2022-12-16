class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            l, r = i + 1, len(num) - 1
            while l < r:
                summa = num[i] + num[l] + num[r]
                if summa == target:
                    return summa
                if abs(summa - target) < abs(result - target):
                    result = summa
                if summa < target:
                    l += 1
                elif summa > target:
                    r -= 1
        return result


"""TESTS:
1)Runtime 1003 ms
Beats 86.40%
Memory
13.9 MB
Beats 61.84%
2)Runtime 1014 ms
Beats 85.72%
Memory 14 MB
Beats 24.16%"""