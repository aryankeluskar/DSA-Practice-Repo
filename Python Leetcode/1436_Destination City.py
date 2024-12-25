from typing import List
from collections import defaultdict


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_map = defaultdict(list)
        for i in paths:
            print(i)
            city_map[i[0]] = i[1]

        currCity = paths[0][1]
        print(currCity in city_map.keys())
        while currCity in city_map.keys():
            print(currCity)
            currCity = city_map[currCity]

        return str(currCity)


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
solution = Solution()
solution.destCity(paths=paths)
