from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cc = [0]*len(nums)*2
        for i in range(len(nums)):
            cc[i] = nums[i]
            cc[len(nums) + i] = nums[i]
        return cc


def main():
    solution = Solution()
    nums = [1, 2, 3]
    result = solution.getConcatenation(nums)
    print(result)


if __name__ == "__main__":
    main()
