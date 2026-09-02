class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        s = 1
        ln = len(nums)
        plist = [1] * ln
        slist = [1] * ln
        output = [1] * ln
        for i in range(1,ln):
            plist[i] = nums[i-1]*p
            p *= nums[i-1]
        
        for i in range(ln-2,-1,-1):
            slist[i] = nums[i+1]*s
            s *= nums[i+1]
        
        for i in range(ln):
            output[i] = slist[i] * plist[i]

        return output