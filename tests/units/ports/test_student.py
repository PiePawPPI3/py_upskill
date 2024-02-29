import pytest

from ports.student import Student


class TestStudent:

    @pytest.mark.parametrize('student_name,scores,expected_result',
                             [('Tomek', [2.0, 2.0, 2.0], True),
                              ('Romek', [2.5, 3.0], False),
                              ('Atomek', [2.0, 2.0, 2.0, 1.0], False),
                              ('Pawel', [1.0, 2.0], False)])
    def test_has_student_passed(self, student_name: str, scores: list[float], expected_result: bool) -> None:
        student = Student(student_name, scores)
        result = student.has_student_passed()
        assert result is expected_result

    @pytest.mark.parametrize('student_name,scores,expected_result',
                             [('Tomek', [3.0, 3.0, 5.0, 5.0], 4.0),
                              ('Romek', [1.0, 1.0, 2.0, 5.0], 2.2),
                              ('Atomek', [3.0], 3.0),
                              ('Pawel', [], 0)])
    def test_calculate_average(self, student_name: str, scores: list[float], expected_result: float) -> None:
        student = Student(student_name, scores)
        result = student.calculate_average()
        assert result == expected_result
