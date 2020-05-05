#!/usr/bin/env python


class Solution(object):
    def maxSubArray(self, nums):

        if len(nums) == 0:
            return 0

        preSum = maxSum = nums[0]
        for i in xrange(1, len(nums)):
            preSum = max((preSum + nums[i]), nums[i])
            print("i=%d, preSum=%d" % (i, preSum))
            maxSum = max(maxSum, preSum)
            print("i=%d, maxSum=%d" % (i, maxSum))
        return maxSum


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print result
