class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        
        for i in range(0, len(nums)):
            needed = target - nums[i]
            if needed in dictionary:
                return [dictionary[needed], i]
            dictionary[nums[i]] = i
        return []