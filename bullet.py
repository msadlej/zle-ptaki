from math import cos, sin, pi
from typing import List, Tuple
from target import Target
from matplotlib import pyplot as plt


MAX_X = 32
MAX_Y = 16
MAX_FORCE = 25
GRAVITY = 9.81
TIME_STEP = 0.01


class InvalidAngleError(Exception):
    pass


class InvalidForceError(Exception):
    pass


class Bullet:
    """
    Class Bullet. Contains attributes:
    :param angle: angle at which the bullet was fired
    :param type: float

    :param force: force at which the bullet was fired
    :param type: float

    :param trajectory: the trajectory of the bullet
    :param type: List[Tuple[float, float]]

    :param position_x: x position of the object
    :param type: float

    :param position_y: y position of the object
    :param type: float
    """

    def __init__(self, angle_degrees: float, force_percentage: int) -> None:
        """
        Creates an instance of class Bullet.
        Takes two arguments:
        the angle in degrees, and the percentage of force,
        at which the bullet was fired.
        Raises InvalidAngleError if the angle given
        is not between 1 and 89 degrees.
        Raises InvalidForceError if the force percentage given
        is not between 1 and 100 percent.
        """

        if angle_degrees not in range(1, 90):
            raise InvalidAngleError()
        self._angle = angle_degrees * (pi/180)

        if force_percentage not in range(101):
            raise InvalidForceError()
        self._force = (force_percentage/100) * MAX_FORCE

        self._trajectory = []
        self._position_x = 0
        self._position_y = 0

    @property
    def angle(self) -> float:
        """
        Returns the angle of the bullet.
        """

        return self._angle

    @property
    def force(self) -> float:
        """
        Returns the force of the bullet.
        """

        return self._force

    @property
    def trajectory(self) -> List[Tuple[float, float]]:
        """
        Returns the trajectory of the bullet.
        """

        return self._trajectory

    @property
    def position(self) -> Tuple[int, int]:
        """
        Returns the position of the bullet.
        """

        return round(self._position_x), round(self._position_y)

    def check_position(self) -> bool:
        """
        Checks if the bullet is inside bounds.
        """

        if self._position_x > MAX_X:
            return False
        if self._position_y < 0:
            return False
        if self._position_y > MAX_Y:
            return False
        return True

    def calculate_trajectory(self, targets: List[Target]) -> Target:
        """
        Calculates the trajectory of the bullet.
        Stores the trajectory in a list.
        Returns the target that was hit.
        If the bullet missed, returns None.
        """

        velocity_x = self.force * cos(self.angle)
        velocity_y = self.force * sin(self.angle)
        time = 0

        while self.check_position():
            self._trajectory.append((self._position_x, self._position_y))

            for target in targets:
                if self.position in target.position:
                    return target

            self._position_x = velocity_x * time
            self._position_y = velocity_y * time
            self._position_y -= 0.5 * GRAVITY * time**2
            time += TIME_STEP

        return None

    @staticmethod
    def draw() -> plt.Circle:
        """
        Returns a plot representation of the bullet.
        """

        return plt.Circle((0, 0), 0.5, color="red")
