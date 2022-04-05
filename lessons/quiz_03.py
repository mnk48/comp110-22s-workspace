"""QZ03 function writing practice."""


class ChristmasTreeFarm:
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        """Initializes the Christmas Tree Farm."""
        self.plots = []
        i: int = 0
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 1

    def plant(self, index: int) -> None:
        """Plants baby trees at a specified index.""" 
        self.plots[index] = 1

    def growth(self) -> None:
        """Grows each tree by 1."""
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] != 0:
                self.plots[i] += 1
            i += 1
    
    def harvest(self, replant: bool) -> int:
        """Decides whether trees will be replanted."""
        tree_count: int = 0
        if replant:
            i: int = 0
            while i < len(self.plots):
                if self.plots[i] >= 5:
                    self.plots[i] = 1
                    tree_count += 1
                i += 1
        else:
            i: int = 0
            while i < len(self.plots):
                if self.plots[i] >= 5:
                    self.plots[i] = 0
                    tree_count += 1
                i += 1
        return tree_count

    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Overload addition to create new ChristmasTreFarm."""
        new_farm: ChristmasTreeFarm 
        size: int = len(self.plots) + len(rhs.plots)
        plantings: int = 0
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] != 0:
                plantings += 1
            i += 1
        i: int = 0
        while i < len(rhs.plots):
            if rhs.plots[i] != 0:
                plantings += 1
            i += 1
        new_farm: ChristmasTreeFarm = ChristmasTreeFarm(size, plantings)
        return new_farm


class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        """"""
        valid: bool 
        if prereq in self.prerequisites and (self.level >= 400):
            valid = True
        else:
            valid = False
        return valid


def find_courses(courses: list[Course], prereq: str) -> list[str]:
    """"""
    classes: list[str] = []
    for course in courses:
        if prereq in course.prerequisites and (course.level >= 400):
            classes.append(course.name)
    return classes 


        