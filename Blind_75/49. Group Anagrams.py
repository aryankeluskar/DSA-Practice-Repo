class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        res = {}

        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_string in res.keys():
                res[sorted_string].append(string)
            else:
                res[sorted_string] = [string]

        return list(res.values())