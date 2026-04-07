class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_inserted_index = 0
        last_inserted = nums[last_inserted_index]
        ptr = 1
        while ptr < len(nums):
            current_number = nums[ptr]
            if current_number > last_inserted:
                last_inserted_index = last_inserted_index + 1
                nums[last_inserted_index] = current_number
                last_inserted = current_number
            ptr += 1
        return last_inserted_index + 1
        