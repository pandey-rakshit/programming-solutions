class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in candies:
            candies.append(i+extraCandies)
            if(max(candies) == i + extraCandies):
                result.append(True)
            else:
                result.append(False)
            
            candies.pop()
        return result