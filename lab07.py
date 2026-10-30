def count_occurrences(target, values):
    #   Base case: an empty list contains it 0 times.
    if (len(values) == 0):
        return 0
    #   Recursive case: 1 (if the first item equals `target`, otherwise 0) plus the count in the rest of the list, values[1:]

    if (values[0] == target):
        return count_occurrences(target, values[1:]) + 1
    else:
        return count_occurrences(target, values[1:])

    


def is_sorted(values):
    # Base case: If there is 0 values or 1 value, it is considered sorted
    if len(values) <= 1:
        return True
    #   Recursive case: the first two items are in order & the rest is sorted.
    if (values[0] <= values[1]):
        return is_sorted(values[1:])
    else:
        return False


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{self.width}x{self.height}"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


def main():
    # Optional scratch space - try your work here, then run: python lab07.py
    # print(count_occurrences(2, [1, 2, 2, 3, 2]))   # 3
    # print(is_sorted([1, 2, 3]))                    # True
    # print(Rectangle(3, 4).area())                  # 12
    # print(Square(5))                               # 5x5
    pass


if __name__ == "__main__":
    main()
