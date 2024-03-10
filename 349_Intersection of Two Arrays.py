class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ma = {}
        for i in nums1:
            ma[i] = True
        
        fin = []
        for i in nums2:
            try:
                if ma[i] and i not in fin:
                    fin.append(i)
            except:
                continue

        return fin