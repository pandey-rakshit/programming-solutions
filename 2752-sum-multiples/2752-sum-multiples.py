class Solution:
    def sumOfMultiples(self, n: int) -> int:
        arr = []
        for i in range(1, n+1):
            if i % 3 == 0:
                arr.append(i)
            elif i % 5 == 0:
                arr.append(i)
            elif i % 7 == 0:
                arr.append(i)
        
        return sum(arr)