"""Final Exam Practice Questions."""


def reverse_multiply(input: list[int]) -> list[int]:
    """Returns an inputed list of ints in reverse order and multiplied."""
    output: list[int] = []
    i: int = len(input) - 1
    while i >= 0: 
        output.append(input[i] * 2)
        i -= 1
    return output


def free_biscuits(input: dict[str, list[int]]) -> dict[str, bool]:
    """Returns a dict of basketball games and if their total points add up to 100."""
    output: dict[str, bool] = {}
    for key in input:
        i: int = 0
        total: int = 0
        while i < len(input[key]):
            total += input[key][i]
            i += 1
        output[key] = (total >= 100)
    return output


def multiples(input: list[int]) -> list[bool]:
    """Returns a list of bools telling if the int value is a multiple of the previous."""
    output: list[bool] = []
    i: int = 0
    while i < len(input):
        if i == 0:
            output.append(input[0] % input[len(input) - 1] == 0)
        else:
            output.append(input[i] % input[i - 1] == 0)
        i += 1
    return output 


def merge_lists(strings: list[str], numbers: list[int]) -> dict[str, int]:
    """Returns a dictionary mapping strings as keys to numbers."""
    output: dict[str, int] = {}
    if len(strings) != len(numbers):
        return output
    else:
        i: int = 0
        while i < len(strings):
            output[strings[i]] = numbers[i]
            i += 1
        return output


class HotCocoa: 
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int):
        """Initializes HotCocoa."""
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness
    
    def mallow_adder(self, mallows: int) -> None:
        self.marshmallow_count += mallows
        self.sweetness += (mallows * 2)

    def calorie_count(self) -> float:
        count: float = 0
        if self.flavor == "vanilla" or "peppermint":
            count += 30
        else:
            count += 20
        if self.has_whip:
            count += 100
        count += (self.marshmallow_count / 2)
        return count
    

class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, initial_minutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = initial_minutes 

    def add_time(self, amount: int) -> None:
        self.minutes += amount
        
    def reset(self) -> int:
        temp: int = self.minutes
        self.minutes = 0
        return temp

    def report(self) -> str:
        hours: int = (self.minutes // 60)
        min: int = (self.minutes % 60)
        return f"{self.name} has spent {hours} hours and {min} minutes on {self.purpose}."