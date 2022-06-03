
from number_of_students_unable_to_eat_lunch import Solution


def test_solution():
    s = Solution()
    students = [1, 1, 0, 0]
    sandwiches = [0, 1, 0, 1]

    ret = s.countStudents(students, sandwiches)
    expected_result = 0

    assert ret == expected_result

    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]

    ret = s.countStudents(students, sandwiches)
    expected_result = 3

    assert ret == expected_result
