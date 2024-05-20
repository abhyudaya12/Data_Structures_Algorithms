#Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
#Beats 94.7% solutions in runtime and 89% in memory

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        a = (new_nums[len(nums)-1])-1
        b = (new_nums[len(nums)-2])-1
        
        return a*b
