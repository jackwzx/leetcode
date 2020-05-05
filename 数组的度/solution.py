#!/usr/bin/env python

class Solution(object):
    def answer(self, nums):
        dict = {}
        maxRepeat = 0
        maxRepeatValue = 0
        for i in range(len(nums)):
            value = int(int(nums[i]))
            if value in dict:
                index = dict[value]
                index.append(i)
                if maxRepeat < len(index):
                    maxRepeat = len(index)
                    maxRepeatValue = value
                elif maxRepeat == len(index):
                    list1 = dict[maxRepeatValue]
                    list2 = dict[value]
                    if list1[-1]-list1[0] > list2[-1]-list2[0]:
                        maxRepeat = len(index)
                        maxRepeatValue = value
            else:
                dict[value] = [i]

        return dict[maxRepeatValue][-1] - dict[maxRepeatValue][0] + 1

if __name__ == '__main__':
    aList = raw_input()
    solution = Solution()
    aList = aList.replace(' ', '')
    numsList = aList.split(',')
    result = solution.answer(numsList)
    print(result)
