class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            ans = nums[i]
            j = i

            while j > 0 and nums[j - 1] > ans:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = ans