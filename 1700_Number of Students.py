from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches:
            if all(val != sandwiches[0] for val in students):
                break
            if students[0] == sandwiches[0]:
                sandwiches.remove(sandwiches[0])
                students.remove(students[0])
            else:
                students.append(students[0])
                students.remove(students[0])

        return len(students)


s = Solution()
print(s.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
