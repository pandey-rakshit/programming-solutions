class Solution:

    def findSmallest(nums, n):
        count = 0
        for i in nums:
            if (n > i):
                count += 1
        return count



    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            scount = Solution.findSmallest(nums, i)
            result.append(scount)
        return result

