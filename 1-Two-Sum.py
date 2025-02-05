class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #brute force method
        #     nums_size = len(nums)
        #     for i in range (nums_size):
        #         for j in range (nums_size-1):
        #             if nums[i]+nums[j+1] == target:
        #                 return [i, j+1]
        #                 break

        nums_size = len(nums)
        for i in range (nums_size):
            comp_value = nums[0]
            nums.remove(nums[0])
            if (target - comp_value) in nums:
                 for j in range(len(nums)):
                    if comp_value+nums[j] == target:
                        return [i, (i+j+1)]
                        break