class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(numRows):
            if i == 0:
                arr.append([1])
            if i == 1:
                arr.append([1,1])
                
            if i > 1:
                lst = arr[i-1]
                temp = [1]
                for i in range(i-1):
                    sumLst = lst[i] + lst[i+1]
                    temp.append(sumLst)
                temp.append(1)
                arr.append(temp)
            
        return arr

