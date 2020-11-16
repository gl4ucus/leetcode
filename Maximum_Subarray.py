class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         target = max(nums)
        
#         max_val = -math.inf
        
#         for i in range(len(nums)):
#             local_sum = nums[i]

#             for j in range(len(nums[i+1:])):
#                 if local_sum > max_val:
#                     max_val = local_sum
#                 elif local_sum < 0:
#                     break
#                 local_sum += nums[i+1+j]
                
#             if local_sum > max_val:
#                 max_val = local_sum
                
#         return(max_val)

        currentsum = nums[0]
        maxsum = nums[0]

        # For each number, will it be bigger by itself? or bigger together when added with the currentsum
        for i in range(1, len(nums)):
            currentsum = max(nums[i], currentsum + nums[i])
            maxsum = max(maxsum, currentsum)
        return maxsum