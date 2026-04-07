class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        while left < n:
            while left < n and nums[left] != val:
                left += 1
            right = left + 1
            while right < n and nums[right] == val:
                right += 1
            if not right < n:
                break
            nums[left], nums[right] = nums[right], nums[left]
        return left