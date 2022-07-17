class Distance:
    # Write your code here
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f'"Distance : {self.km} kilometers"'

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, int):
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, other):
        if isinstance(other, int):
            return Distance(self.km * other)
        else:
            return Distance(self.km * other.km)

    def __truediv__(self, divider):
        if isinstance(divider, (int, float)):
            return Distance(round(self.km / divider, 2))

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other):
        if isinstance(other, int):
            return self.km == other
        return self.km == other.km

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __len__(self):
        return self.km
