
from timeit import timeit
from dataclasses import dataclass, field

# https://realpython.com/python-range-membership-test/

numbers_as_range = range(10_000_000)
numbers_as_list = list(numbers_as_range)

# formula check of the number
print(timeit("-1 in numbers_as_range", globals=globals(), number=100))

# sequential check of all items in the list
print(timeit("-1 in numbers_as_list", globals=globals(), number=100))


# our own implementation of the range and its iterator
@dataclass
class Range:
    start: int
    stop: int
    step: int = 1

    def __iter__(self):
        return _RangeIterator(self.start, self.stop, self.step)

    def __contains__(self, element):
        return (
            self.start <= element < self.stop
            and (element - self.start) % self.step == 0
        )

@dataclass
class _RangeIterator:
    start: int
    stop: int
    step: int
    _state: int | None = field(default=None, init=False)

    def __next__(self):
        if self._state is None:
            self._state = self.start
        else:
            self._state += self.step
        if self._state >= self.stop:
            raise StopIteration
        return self._state

# range converted to list
print(list(Range(start=1, stop=10, step=2)))

# check of numbers in the range
print(7 in Range(start=1, stop=10, step=2))
print(4 in Range(start=1, stop=10, step=2))

# our check against the range
numbers = Range(0, 10_000_000)
print(timeit("-1 in numbers", globals=globals(), number=100))

