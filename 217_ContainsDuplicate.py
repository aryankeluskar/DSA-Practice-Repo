# December 8, 2023


class Solution(object):
    def FirstContainsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = []
        for i in range(len(nums) - 1):
            seen.append(nums[i])
            if nums[i + 1] in seen:
                return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


def main():
    nums = [1, 2, 3, 4, 5, 6, 6, 8, 9, 10]
    solution = Solution()
    result = solution.FirstContainsDuplicate(nums)
    print(result)


if __name__ == "__main__":
    main()
