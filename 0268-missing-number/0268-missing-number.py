class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt == mid + 1:
                left = mid + 1
            else:
                right = mid
        return left