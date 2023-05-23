class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        k = 0
        y = n
        arr = []

        while k != n:
            arr.append(nums[k])
            arr.append(nums[y])
            k += 1
            y += 1

        return arr
        