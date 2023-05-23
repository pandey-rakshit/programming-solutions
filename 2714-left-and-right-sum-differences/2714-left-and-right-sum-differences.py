class Solution:

    def findLeftSum(nums): 
        sum = 0
        arr = []
        for i in nums:
            arr.append(sum)
            sum += i
        return arr

    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = Solution.findLeftSum(nums)
        rev = nums[::-1]
        temp = Solution.findLeftSum(rev)
        rightSum = temp[::-1]
        result = []
        for i in range(len(nums)):
            difference = leftSum[i] - rightSum[i]
            if difference < 0:
                difference *= -1
            result.append(difference)
        return result
