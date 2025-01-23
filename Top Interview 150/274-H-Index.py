from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sortedList = sorted(citations, reverse=True)
        hmax=0
        for i in range(len(sortedList)):
            if sortedList[i]>=i+1:
                hmax+=1
        return hmax


solution = Solution() 
# Testcase 1. Output: 3
citations = [3,0,6,1,5]
print(solution.hIndex(citations))

# Testcase 1. Output: 1
citations = [1,3,1]
print(solution.hIndex(citations))