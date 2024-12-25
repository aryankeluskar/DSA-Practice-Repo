class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            original_length = len(seen)
            seen.add(i)

            if original_length == len(seen):
                return True

        return False