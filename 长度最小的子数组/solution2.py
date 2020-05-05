#!/usr/bin/env python

limit = 7


class Solution(object):

    @staticmethod
    def answer(nums):
        l_sum = 0
        j = 0
        ans = float("inf")
        for i in range(len(nums)):
            while j < len(nums) and l_sum < limit:
                l_sum += nums[j]
                j += 1
            if l_sum >= limit:
                ans = min(ans, j - i)
                l_sum -= nums[i]

        return ans if ans != float("inf") else 0


if __name__ == '__main__':
    solution = Solution()
    result = solution.answer([2, 3, 1, 2, 4, 3])
    print(result)
