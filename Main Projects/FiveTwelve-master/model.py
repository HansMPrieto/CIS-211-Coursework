"""Hans Prieto
FiveTwelve Project
The game state and logic (model component) of 512, 
a game based on 2048 with a few changes. 
This is the 'model' part of the model-view-controller
construction plan.  It must NOT depend on any
particular view component, but it produces event 
notifications to trigger view updates. 
"""

from game_element import GameElement, GameEvent, EventKind

from typing import List, Tuple, Optional
import random

# Configuration constants
GRID_SIZE = 4

class Vec():
    """A Vec is an (x,y) or (row, column) pair that
    represents distance along two orthogonal axes.
    Interpreted as a position, a Vec represents
    distance from (0,0).  Interpreted as movement,
    it represents distance from another position.
    Thus we can add two Vecs to get a Vec.
    """
    def __init__(self, x: int, y: int):
        """x is row, y is column"""
        self.x = x
        self.y = y

    def __add__(self, other: "Vec") -> "Vec":
        """adds the x and y values between two vectors"""
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return Vec(sum_x, sum_y)

    def __eq__(self, other: "Vec") -> bool:
        """Determines whether two vectors are the same"""
        return self.x == other.x and self.y == other.y

class Tile(GameElement):
    """A slidy numbered thing."""
    def __init__(self, pos: Vec, value: int):
        """position is vector, value is an integer."""
        super().__init__()
        self.row = pos.x
        self.col = pos.y
        self.value = value

    def __repr__(self):
        """Not like constructor --- more useful for debugging"""
        return f"Tile[{self.row},{self.col}]:{self.value}"

    def __str__(self):
        """represents the value of a tile as a string"""
        return str(self.value)

    def move_to(self, new_pos: Vec):
        "Moves a tile to a new position"
        self.row = new_pos.x
        self.col = new_pos.y
        self.notify_all(GameEvent(EventKind.tile_updated, self))

    def __eq__(self, other: "Tile"):
        """Determines whether the value of two tiles are the same"""
        return self.value == other.value

    def merge(self, other: "Tile"):
        """Merges two tiles with each other"""
        # This tile incorporates the value of the other tile
        self.value = self.value + other.value
        self.notify_all(GameEvent(EventKind.tile_updated, self))
        # The other tile has been absorbed.  Resistance was futile.
        other.notify_all(GameEvent(EventKind.tile_removed, other))

class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """

    def __init__(self, rows=4, cols=4):
        """rows is x, columns is y."""
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.tiles = [ ]
        for row in range(rows):
            row_tiles = [ ]
            for col in range(cols):
                row_tiles.append(None)
            self.tiles.append(row_tiles)

    def __getitem__(self, pos: Vec) -> Tile:
        """Gets the tile of a certain position."""
        return self.tiles[pos.x][pos.y]

    def __setitem__(self, pos: Vec, tile: Tile):
        """Sets a value to a tile"""
        self.tiles[pos.x][pos.y] = tile

    def _empty_positions(self) -> list:
        """Return a list of positions of None values,
            i.e., unoccupied spaces.
            """
        empties = []
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                if self.tiles[row][col] is None:
                    empties.append(Vec(row, col))
        return empties

    def has_empty(self) -> bool:
        """Is there at least one grid element without a tile?"""
        if len(self._empty_positions()) > 0:
            return True
        else:
            return False

    def place_tile(self,value=None):
        """Place a tile on a randomly chosen empty square."""
        empties = self._empty_positions()
        assert len(empties) > 0
        choice = random.choice(empties)
        row = choice.x
        col = choice.y
        if value is None:
            # 0.1 probability of 4
            if random.random() < 0.1:
                value = 4
            else:
                value = 2
        new_tile = Tile(Vec(row, col), value)
        self.tiles[row][col] = new_tile
        self.notify_all(GameEvent(EventKind.tile_created, new_tile))

    def to_list(self) -> List[List[int]]:
        """Test scaffolding: represent each Tile by its
        integer value and empty positions as 0
        """
        result = [ ]
        for row in self.tiles:
            row_values = []
            for col in row:
                if col is None:
                    row_values.append(0)
                else:
                    row_values.append(col.value)
            result.append(row_values)
        return result

    def from_list(self, values: List[List[int]]):
        """Test scaffolding: set board tiles to the
        given values, where 0 represents an empty space.
        """
        result = [ ]
        for row in range(len(values)):
            row_values = []
            for col in range(len(values[row])):
                if values[row][col] == 0:
                    row_values.append(None)
                else:
                    board_tile = Tile(Vec(row, col), values[row][col])
                    row_values.append(board_tile)
            result.append(row_values)
        self.tiles = result

    def in_bounds(self, pos: Vec) -> bool:
        """Is position (pos.x, pos.y) a legal position on the board?"""
        return 0 <= pos.x <= self.rows-1 and 0 <= pos.y <= self.cols-1

    def slide(self, pos: Vec, dir: Vec):
        """Slide tile at row,col (if any)
        in direction (dx,dy) until it bumps into
        another tile or the edge of the board.
        """
        if self[pos] is None:
            return
        while True:
            new_pos = pos + dir
            if not self.in_bounds(new_pos):
                break
            if self[new_pos] is None:
                self._move_tile(pos, new_pos)
            elif self[pos] == self[new_pos]:
                self[pos].merge(self[new_pos])
                self._move_tile(pos, new_pos)
                break  # Stop moving when we merge with another tile
            else:
                # Stuck against another tile
                break
            pos = new_pos

    def _move_tile(self, old_pos: Vec, new_pos: Vec):
        """Moves a tile."""
        self[old_pos].move_to(new_pos)
        self.tiles[new_pos.x][new_pos.y] = self.tiles[old_pos.x][old_pos.y]
        self.tiles[old_pos.x][old_pos.y] = None

    def down(self):
        """Slides a tile down."""
        down_cur = Vec(self.rows-1, 0)
        down_outer_loop_increment = Vec(0, 1)
        down_inner_loop_increment = Vec(-1, 0)
        down_dir = Vec(1, 0)
        self._move(down_cur, down_outer_loop_increment, down_inner_loop_increment, down_dir)

    def up(self):
        """Slides a tile up."""
        up_cur = Vec(0, 0)
        up_outer_loop_increment = Vec(0, 1)
        up_inner_loop_increment = Vec(1, 0)
        up_dir = Vec(-1, 0)
        self._move(up_cur, up_outer_loop_increment, up_inner_loop_increment, up_dir)

    def right(self):
        """Slides a tile to the right."""
        right_cur = Vec(0, self.cols-1)
        right_outer_loop_increment = Vec(1, 0)
        right_inner_loop_increment = Vec(0, -1)
        right_dir = Vec(0, 1)
        self._move(right_cur, right_outer_loop_increment, right_inner_loop_increment, right_dir)

    def left(self):
        """Slides a tile to the left."""
        left_cur = Vec(0, 0)
        left_outer_loop_increment = Vec(1, 0)
        left_inner_loop_increment = Vec(0, 1)
        left_dir = Vec(0, -1)
        self._move(left_cur, left_outer_loop_increment, left_inner_loop_increment, left_dir)

    def _move(self, cur: Vec, outer_loop_increment: Vec, inner_loop_increment: Vec, dir: Vec):
        """Move method for sliding a tile either down, up, right, or left"""
        while self.in_bounds(cur):
            saved = cur
            while self.in_bounds(cur):
                self.slide(cur, dir)
                cur = cur + inner_loop_increment
            cur = saved + outer_loop_increment

    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        score = 0
        tiles = self.to_list()
        for row_values in tiles:
            for col_value in row_values:
                score += col_value
        return score
