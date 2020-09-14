"""Hans Prieto
Professor Michal Young"""

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        """Move to (x+dx, y + dy)"""
        self.x += dx
        self.y += dy

    def __eq__(self, other: "Point") -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return f"({self.x}, {self.y})"
