class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def consume(nums: list[int], entry: int, dup_buffer : list[int]):
            i = entry + 1
            while i < len(nums) and nums[i] == nums[entry]:
                dup_buffer.append(nums[i])
                i += 1
            next_entry = i
            return next_entry

        dup_buffer = []
        pos = 0
        entry = 0
        while entry < len(nums):
            entry = consume(nums, entry, dup_buffer)
            pos += 1
            if entry == len(nums) and pos < len(nums):
                nums[pos] = nums[entry - 1]
            elif entry == len(nums) and pos == len(nums):
                nums[pos - 1] = nums[entry - 1]
            else:
                nums[pos] = nums[entry]
        k = pos
        for j in range(len(dup_buffer)):
            nums[pos + j] = dup_buffer[j]
        return k

            