class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for index, value in enumerate(nums):
            
            if (target-value) in hashmap:
                return [hashmap[target-value],index]
            hashmap[value]=index

sol = Solution()
print(sol.twoSum([3, 3, 4, 5],6))