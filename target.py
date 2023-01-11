from typing import List, Tuple
from matplotlib import pyplot as plt


class InvalidPositionError(Exception):
    pass


class InvalidHeightError(Exception):
    pass


class InvalidHealthError(Exception):
    pass


class Target:
    """
    Class Target. Contains attributes:
    :param position_x: x position of the object
    :param type: int

    :param position_y: y position of the object
    :param type: int
    """

    def __init__(self, position_x: int, position_y: int) -> None:
        """
        Creates an instance of class Target.
        Takes two arguments:
        the x and y position of the target.
        Raises InvalidPositionError if the position given
        is less than 0.
        """

        if position_x < 0 or position_y < 0:
            raise InvalidPositionError()

        self._position_x = position_x
        self._position_y = position_y

    @property
    def position(self) -> List[Tuple[int, int]]:
        """
        Returns the position of the target.
        """

        return [(self._position_x, self._position_y)]

    def hit(self) -> bool:
        """
        Simulates the Target being hit.
        Returns True, as the target is always destroyed after one hit.
        """

        return True

    def draw(self) -> plt.Circle:
        """
        Returns a plot representation of class target.
        """

        plot_position = self.position[0]
        radius = 0.5
        color = "green"
        return plt.Circle(plot_position, radius, color=color)

    def __str__(self) -> str:
        """
        Returns a string representation of class Target.
        """

        return "Target"


class Obstacle(Target):
    """
    Class Obstacle. Contains attributes:
    :param height: height of the obstacle
    :param type: int
    """

    def __init__(self, position_x: int, height: int) -> None:
        """
        Creates an instance of class Obstacle.
        Takes two arguments:
        the x position and the height of the obstacle.
        The y position of the obstacle is always 0.
        Raises InvalidHeightError if the height given
        is less than 1.
        """

        if height < 1:
            raise InvalidHeightError()

        self._height = height
        super().__init__(position_x, 0)

    @property
    def height(self) -> int:
        return self._height

    @property
    def position(self) -> List[Tuple[int, int]]:
        """
        Returns the position of the obstacle.
        """

        return [(self._position_x, y) for y in range(self._height)]

    def hit(self) -> bool:
        """
        Simulates the Obstacle being hit.
        Returns False, as the obstacle cannot be destroyed.
        """

        return False

    def draw(self) -> plt.Rectangle:
        """
        Returns a plot representation of class obstacle.
        """

        plot_position = (self._position_x - 0.5, 0)
        width = 1
        height = self.height - 0.5
        color = "saddlebrown"
        return plt.Rectangle(plot_position, width, height, color=color)

    def __str__(self) -> str:
        """
        Returns a string representation of class Obstacle.
        """

        return "Obstacle"


class Boss(Target):
    """
    Class Boss. Contains attributes:
    :param health: health of the boss
    :param type: int
    """

    def __init__(self, position_x: int, position_y: int, health: int) -> None:
        """
        Creates an instance of class Boss.
        Takes three arguments:
        the x and y position of the target,
        and the health of the boss.
        Raises InvalidHealthError if the health given
        is less than 1.
        """

        if health < 1:
            raise InvalidHealthError()

        self._health = health
        super().__init__(position_x, position_y)

    @property
    def health(self) -> int:
        return self._health

    @property
    def position(self) -> Tuple[int]:
        """
        Returns the position of the Boss.
        """

        x = self._position_x
        y = self._position_y
        return [(x, y), (x + 1, y),
                (x, y + 1), (x + 1, y + 1)]

    def hit(self) -> bool:
        """
        Simulates the boss being hit.
        Removes one point of health from the boss.
        Returns true if the boss was destroyed, False otherwise.
        """

        self._health -= 1

        if self._health == 0:
            return True
        return False

    def draw(self) -> plt.Circle:
        """
        Returns a plot representation of class boss.
        """

        plot_position = (self._position_x + 0.5, self._position_y + 0.5)
        radius = 1
        color = "blue"
        return plt.Circle(plot_position, radius, color=color)

    def __str__(self) -> str:
        """
        Returns a string representation of class Boss.
        """

        return "Boss"
