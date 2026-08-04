class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums): # each no in the array as first value
            if i > 0 and a == nums[i - 1]: # i > 0 isnt the value in the first value in the input array and a ==nums[i- 1] dont wanna use the same value twice
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a +nums[l] + nums[r]
                if threeSum > 0:
                    r-= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                    






