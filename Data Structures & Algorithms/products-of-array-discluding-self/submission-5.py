class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])
        suffix = [1]*len(nums)
        for j in range(len(nums)-2,-1,-1):
            suffix[j] = suffix[j+1] * nums[j+1]
        output = []
        for i in range(len(nums)):
            output.append(prefix[i]*suffix[i])
        return output