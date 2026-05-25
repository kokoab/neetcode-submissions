class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for current_index, num in enumerate(nums):
            difference = target - num

            if difference in seen:
                return [seen[difference], current_index]

            seen[num] = current_index
        

            





