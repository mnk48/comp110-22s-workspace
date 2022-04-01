"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730389267"


class Simpy:
    values: list[float]

    def __init__(self, values):
        """Initializes Simpy's values to the inputed values list."""
        self.values = values
    
    def __str__(self) -> str:
        """Returns a string representation of a Simpy object."""
        return f"Simpy({str(self.values)}"
    
    def fill(self, input: float, number: int) -> None:
        """Given a inputed float and length, fills a Simpy's values with that float and given length."""
        self.values = []
        i: int = 0
        while i < number:
            self.values.append(input)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Given a start, stop, and step float, mutates a Simpy object to produce a list of floats starting with the start index,
        ending with the number before the stop index, and increasing or decreasing by the step index.
        """
        self.values = []
        i: int = 0
        while (start + (i * step)) != stop:
            self.values.append(start + (i * step))
            i += 1
    
    def sum(self) -> float:
        """Calculates the sum of the values within a Simpy object list."""
        result: float = sum(self.values)
        return result
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Given a float or a Simpy object, adds the float values to each self index
        or the corresponding Simpy indices together to return a new Simpy object.
        """
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            i: int = 0
            while i < len(rhs.values):
                result.values.append(rhs.values[i] + self.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs)
                i += 1 
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Given a float or a Simpy, raises the values of the Simpy object to that
        float or corresponding Simpy index.
        """
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            i: int = 0 
            while i < len(rhs.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs)
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Given a Simpy and either a float or Simpy, returns a list of bools 
        describing whether the index at the simpy equals the float or the index at the rhs Simpy.
        """
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs)
                i += 1
        return result    
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Given a float or Simpy, results a list of bools describing whether the self at the index
        is greater than the float or the Simpy at the index.
        """
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs)
                i += 1
        return result
    
    def __getitem__(self, rhs: int) -> float:
        """"""
        return self.values[rhs]
        