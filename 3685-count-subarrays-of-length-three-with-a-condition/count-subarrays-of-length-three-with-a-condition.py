class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count=0
        for i in range(0,len(nums)-2):
            if (nums[i]+nums[i+2])*2==nums[i+1]:
                count=count+1
        return count