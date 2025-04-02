class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        result = [1] * n
        prefix_product = [1] * n
        suffix_product = [1] * n
        # Calculate de products at the left (prefix)
        
        for i in range (1,n):
            prefix_product[i] = prefix_product[i-1]*nums[i-1]

        
        suffix_product = 1
        for i in range(n-1,-1,-1):
            result[i] = prefix_product[i]*suffix_product
            suffix_product*= nums[i]
            
            

        return result
    
sol = Solution()
print("result",sol.productExceptSelf([1,2,3,4]))
