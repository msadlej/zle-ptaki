from target import Target
from bullet import Bullet, MAX_X, MAX_Y
from typing import List, Tuple
from matplotlib import pyplot as plt
from io import BytesIO


class IvalidAttemptsError(Exception):
    def __init__(self) -> None:
        super().__init__("Number of attempts cannot be less than one!")


class Level:
    """
    Class Level. Contains attributes:
    :param targets: List of taargets on the board
    :param type: List[Target]

    :param attempts: Number of permitted attempts for the level
    :param type: int

    :param result: Result of the Level
    :param type: bool

    :param trajectory: Bullets trajectory
    :param type: trajectory: List[Tuple[float, float]]
    """

    def __init__(self, attempts: int, targets: List[Target]) -> None:
        """
        Creates an instance of class Level.
        Takes three arguments:
        the number of attempts permitted,
        the list of targets on the board
        and the UI window.
        Raises IvalidAttemptsError if the number of attempts given
        is less than 1.
        """

        if attempts < 1:
            raise IvalidAttemptsError()
        self._attempts = attempts
        self._targets = targets
        self._trajectory = []
        self._result = False

    @property
    def attempts(self) -> int:
        """
        Returns the number attempts in the level.
        """

        return self._attempts

    @property
    def targets(self) -> List[Target]:
        """
        Returns the list of targets in the level.
        """

        return self._targets

    @property
    def trajectory(self) -> List[Tuple[float, float]]:
        """
        Returns the Bullets trajectory
        """

        return self._trajectory

    @property
    def result(self) -> bool:
        """
        Returns the result of the level.
        """

        return self._result

    def draw_board(self) -> BytesIO:
        """
        Creates a pyplot figure representing the current
        state of the board.
        """

        plt.close()
        plt.clf()
        plt.figure(figsize=(8, 4), dpi=200)
        plt.xlim(0, MAX_X + 1)
        plt.ylim(0, MAX_Y + 1)
        plt.xticks([])
        plt.yticks([])

        fig = plt.gcf()
        ax = fig.gca()
        ax.add_patch(Bullet.draw())
        for target in self.targets:
            ax.add_patch(target.draw())

        buffer = BytesIO()
        fig.savefig(buffer)
        return buffer

    def draw_trajectory(self) -> BytesIO:
        """
        Draws the bullets trajectory on the board.
        """

        x = [p[0] for p in self.trajectory]
        y = [p[1] for p in self.trajectory]
        plt.plot(x, y, ':', color="black")

        buffer = BytesIO()
        plt.savefig(buffer)
        return buffer

    def simulate_attempt(self, angle, force) -> Target:
        """
        Simulates the attempt.
        Takes the angle and force as input.
        Sets result to true if the level was won.
        Returns the Target that was hit.
        """

        bullet = Bullet(angle, force)
        attempt_result = bullet.calculate_trajectory(self.targets)
        self._trajectory = bullet.trajectory
        self._attempts -= 1

        if attempt_result is not None:
            if attempt_result.hit():
                self._targets.remove(attempt_result)
                if all(str(target) == "Obstacle" for target in self.targets):
                    self._result = True

        return attempt_result
