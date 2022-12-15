class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
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