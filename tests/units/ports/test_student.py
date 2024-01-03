from ports.student import Student


class TestHasStudentPassed:
    def test_student_passed(self) -> None:
        student = Student("Pawel", [2.0, 2.0, 2.0])
        result = student.has_student_passed()
        assert result is True

    def test_student_failed_insufficient_scores_number(self) -> None:
        student = Student("Pawel", [2.5, 3.0])
        result = student.has_student_passed()
        assert result is False

    def test_student_failed_low_average(self) -> None:
        student = Student("Pawel", [2.0, 2.0, 2.0, 1.0])
        result = student.has_student_passed()
        assert result is False

    def test_student_failed_low_average_insufficient_scores(self) -> None:
        student = Student("Pawel", [1.0, 2.0])
        result = student.has_student_passed()
        assert result is False


class TestCalculateAverages:
    def test_calculate_average(self) -> None:
        student = Student("Pawel", [3.0, 3.0, 5.0, 5.0])
        result = student.calculate_average()
        assert result == 4.0

    def test_calculate_average_one_score(self) -> None:
        student = Student("Pawel", [3.0])
        result = student.calculate_average()
        assert result == 3.0

    def test_calculate_for_no_scores(self) -> None:
        student = Student("Pawel", [])
        result = student.calculate_average()
        assert result == 0
