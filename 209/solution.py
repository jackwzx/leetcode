#!/usr/bin/env python

limit = 7

class Solution(object):
    def answer(self, nums):
        dict = {}
        begin = 0
        end = 0
        total = 0
        isFirst = False
        for i in range(len(nums)):
            value = nums[i]
            if total + value <= limit: 
                total += value
                end = i 
                print("1= begin=%d end=%d total = %d"%(begin, end, total))
            else:
                if value == nums[begin]:
                    begin += 1
                    end = i
                    print("2= begin=%d end=%d total = %d"%(begin, end, total))
                elif value > nums[begin]:
                    end = i
                    tempSubTotal = nums[begin]
                    print("3= begin=%d end=%d total = %d"%(begin, end, total))

                    while(value > tempSubTotal):
                        begin += 1
                        tempSubTotal += nums[begin]
                        print("4= begin=%d end=%d total = %d"%(begin, end, total))

                    total += value
                    total -= tempSubTotal

        return nums[begin:end+1]


if __name__ == '__main__':
    #aList = raw_input()
    #solution = Solution()
    #aList = aList.replace(' ', '')
    #numsList = aList.split(',')
    #result = solution.answer(numsList)
    solution = Solution()
    result = solution.answer([2,3,1,2,4,3])
    print(result)
