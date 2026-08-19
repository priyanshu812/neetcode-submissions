class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        pre = 1
        suffix = []
        suff = 1 

        for i in range(len(nums)):
            prefix.append(pre)
            pre = pre * nums[i]
        for i in range(len(nums)-1,-1,-1):
            suffix.append(suff)
            suff = suff*nums[i]
        suffix = suffix[::-1]
        for i in range(len(nums)):
            nums[i] = prefix[i] *suffix[i]
        
        return nums
