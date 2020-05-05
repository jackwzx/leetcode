#!/usr/bin/env python

limit = 7

class Solution(object):
    def answer(self, nums):
        sum = 0
        j = 0
        ans = float("inf")
        for i in range(len(nums)):
            while j < len(nums) and sum < limit:
                sum += nums[j]
                j += 1
            if sum >= limit:
                ans = min(ans, j-i)
            sum -= nums[i]

        return ans if ans != float("inf") else 0

if __name__ == '__main__':
    solution = Solution()
    result = solution.answer([2,3,1,2,4,3])
    print(result)