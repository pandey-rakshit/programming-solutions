class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL = 0
        countR = 0
        countResult = 0
        for i in s:
            if i == 'L':
                countL += 1
            elif i == 'R':
                countR += 1

            if countL == countR:
                countResult += 1
                countL = 0
                countR = 0
        return countResult
            
            
