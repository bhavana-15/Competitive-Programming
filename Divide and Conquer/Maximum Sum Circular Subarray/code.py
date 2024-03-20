class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            max_cur=max_glo=nums[0]
            for i in range(1,len(nums)):
                max_cur=max(nums[i],max_cur+nums[i])
                max_glo=max(max_glo,max_cur)
            return max_glo
        firstsum=kadane(nums)
        totalsum=sum(nums)
        secondsum=totalsum+kadane([-x for x in nums])
        return max(firstsum,secondsum) if secondsum!=0 else firstsum
