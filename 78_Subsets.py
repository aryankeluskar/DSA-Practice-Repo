from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        fin = []
        for i in range(2**l):
            # Format the integer as a binary string with leading zeros
            binary_str = format(i, '0' + str(l) + 'b')
            extracted_elements = []
            for j, bit in enumerate(binary_str):
                if bit == '1':
                    extracted_elements.append(nums[j])
            fin.append(extracted_elements)

        return fin
