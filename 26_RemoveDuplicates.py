from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=1
        print(len(nums))
        for fast in range (1,len(nums)):
            
            print(nums[fast   ])
            if nums[fast] != nums[slow-1]:
                nums[slow] = nums[fast]
                slow+=1
        return slow

# Prueba simple
nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Output k: {k}, nums: {nums[:k]}")