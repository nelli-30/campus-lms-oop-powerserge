from base_task import AcademicTask


class Quiz(AcademicTask):
    def __init__(self, title: str, max_points: int, total_questions: int) -> None:
        super().__init__(title, max_points)
        self.__total_questions: int = total_questions
        self.correct_answers: int = 0

    def submit_work(self, correct_answers: int) -> None:
        self.correct_answers = correct_answers
        print(f"Quiz submitted: {self.title}")

    def grade_work(self) -> float:
        self.is_graded = True
        if self.__total_questions == 0:
            return 0.0
        return (self.correct_answers / self.__total_questions) * self.max_points

    def get_details(self) -> None:
        print(
            f"[QUIZ] {self.title} - Max Points: {self.max_points} | "
            f"Questions: {self.__total_questions}"
        )
