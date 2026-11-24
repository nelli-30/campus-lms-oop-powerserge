from abc import ABC, abstractmethod

class AcademicTask(ABC):
    def __init__(self, title: str, max_points: int) -> None:
        self.title: str = title
        self.max_points: int = max_points
        self.is_graded: bool = False

    @abstractmethod
    def submit_work(self) -> None:
        pass

    @abstractmethod
    def grade_work(self) -> None:
        pass

    @abstractmethod
    def get_details(self) -> str:
        pass
