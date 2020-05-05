#!/usr/bin/env python


class Solution(object):

    def maxProduct(self, nums):
        max = 0
        sec = 0
        third = 0
        for i in range(len(nums)):
            value = int(int(nums[i]))
            if max < value:
                third = sec
                sec = max
                max = value
            elif sec < value:
                third = sec
                sec = value
            elif third < value:
                third = value
        return max * sec * third


if __name__ == '__main__':
    aList = raw_input()
    solution = Solution()
    aList = aList.replace(' ', '')
    numsList = aList.split(',')
    result = solution.maxProduct(numsList)
    print(result)
