class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWord = 0
        for i in sentences:
            wordsArr = i.split(" ")
            if maxWord < len(wordsArr):
                maxWord = len(wordsArr)
        return maxWord