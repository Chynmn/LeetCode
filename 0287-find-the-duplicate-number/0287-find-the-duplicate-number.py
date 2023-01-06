class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        
        while left < right:
            mid = left + (right-left)//2
            
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            if count <= mid:
                left = mid + 1
            else:
                right = mid
            
        return left