class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 not in nums:
            product = 1
            for i in nums :
                product = product * i 

            for i in range(len(nums)):
                nums[i] = product//nums[i]


        else:
            num_of_zero = 0 
            for i in nums :
                if i == 0 :
                    num_of_zero += 1 
            if num_of_zero > 1:
                for i in range(len(nums)):
                    nums[i] = 0
            else :
                    product0 =1
                    for i in nums:
                        if i != 0:
                            product0 = product0 * i 
                    for i in range(len(nums)):
                        if nums[i]==0:
                            nums[i] = product0
                        else :
                            nums[i] = 0 
        return nums

        