class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum =0
        for i in nums:
            curSum += i
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum =0
        return maxSum

        
            
        