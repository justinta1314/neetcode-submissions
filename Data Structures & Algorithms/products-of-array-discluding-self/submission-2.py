class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        # First get all numbers on left of current number
        leftProduct = 1
        for i in range(len(nums)):
            res[i] = leftProduct
            leftProduct *= nums[i]
        
        # Then get all numbers on right of current number
        rightProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rightProduct
            rightProduct *= nums[i]
        return res