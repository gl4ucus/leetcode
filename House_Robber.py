class Solution:
    def rob(self, nums: List[int]) -> int:
#         Ver 1
#         Wrong to assume that it is just odd and even numbered houses
#         For instance, [2, 1, 1, 2]
#         odd_nums = nums[1::2]
#         even_nums = nums[0::2]
#         return(max(sum(odd_nums), sum(even_nums)))


#         Ver 2
#         https://www.youtube.com/watch?v=xlvhyfcoQa4&ab_channel=KevinNaughtonJr.
#         If 0 house, nothing to rob.
#         If 1 house, can only rob it.
#         If 2 houses, rob the higher one.
#         If 3 houses, rob 1+3 or 2 
#         If n houses, ...
#         Solve use bottom-up processing 
#         But this requires us to maintain an array!

#         if len(nums) == 0: return 0
#         if len(nums) == 1: return nums[0]
#         if len(nums) == 2: return max(nums)
        
#         dp = []
#         dp.append(nums[0])
#         dp.append(max(nums[0:2]))
#         for i in range(2, len(nums)):
#             dp.append(max(nums[i] + dp[i-2], dp[i-1]))
        
#         print(dp)
#         return dp[-1]

        # Ver 3: No need to maintain an array
        if len(nums) == 0: return 0
        if len(nums) <= 2: return max(nums)
        
        one = nums[0]
        two = max(nums[0:2])
        for i in range(2, len(nums)):
            currentmax = max(nums[i] + one, two)
            one = two
            two = currentmax
        return currentmax