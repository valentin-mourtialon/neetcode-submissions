class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        occ = 0
        for n in nums:
            if n == val:
                occ += 1
        for _ in range(occ):
            nums.remove(val)
        return len(nums)
        