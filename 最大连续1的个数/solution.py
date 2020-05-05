#!/usr/bin/env python


class Solution(object):
    def findMaxConnectOnes(self, nums):
        count = 0
        ans = 0
        print(type(nums))
        for i in range(len(nums)):
            if int(nums[i]) == 1:
                count += 1
            else:
                count = 0
            ans = max(ans, count)

        return ans



if __name__ == '__main__':
    aList = raw_input()
    solution = Solution()
    aList = aList.replace(' ', '')
    numsList = aList.split(',')
    result = solution.findMaxConnectOnes(numsList)
    print(result)

