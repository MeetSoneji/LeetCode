class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        else:
            count=0
            for i in set(nums):
                if i>k:
                    count=count+1
            return count