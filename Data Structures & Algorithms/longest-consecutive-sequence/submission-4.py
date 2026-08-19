class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        out = 1
        if len(nums)>1:

            previous = nums[0]
            output = 1 
            for i in range(1,len(nums)):
                if  nums[i] == previous +1:
                    out += 1 
                    previous += 1 
                    output = max(out,output)
                elif nums[i] == previous :
                    continue

                else :
                    out = 1
                    previous = nums[i]
                    
        elif len(nums) == 1: output = 1
        else: output = 0

        return output

