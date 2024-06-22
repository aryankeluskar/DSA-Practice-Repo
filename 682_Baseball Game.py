from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in operations:
            print(i + "ini " + str(score))
            if i == "C":
                score.pop()
            elif i == "D":
                score.append(int(score[-1]) * 2)
            elif i == "+":
                score.append(int(score[-1]) + int(score[-2]))
            else:
                score.append(int(i))
            print(i + "fin " + str(score))

        return sum(score)
