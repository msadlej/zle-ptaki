from bullet import Bullet, MAX_X, MAX_Y
from target import Target
from typing import List, Tuple
from matplotlib import pyplot as plt


class IvalidAttemptsError(Exception):
    pass


class Level:
    """
    Class Level. Contains attributes:
    :param targets: List of taargets on the board
    :param type: List[Target]

    :param attempts: Number of permitted attempts for the level
    :param type: int
    """

    def __init__(self, attempts: int, targets: List[Target]) -> None:
        """
        Creates an instance of class Level.
        Takes two arguments:
        the number of attempts permitted
        and the list of targets on the board.
        Raises IvalidAttemptsError if the number of attempts given
        is less than 1.
        """

        if attempts < 1:
            raise IvalidAttemptsError()
        self._attempts = attempts
        self._targets = targets

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

    def play(self) -> bool:
        """
        Simulates the level.
        Asks for the angle and force each attempt.
        Returns true if the level was won, false otherwise.
        """

        while self.attempts > 0 and self.targets:
            self.draw_board()
            angle = int(input("Give an angle in degrees:"))
            force = int(input("Give a force percentage:"))
            bullet = Bullet(angle, force)
            result = bullet.calculate_trajectory(self.targets)
            self.draw_trajectory(bullet.trajectory)

            if result is None:
                print("Missed!")
            else:
                print(f"{result} hit!")

                if result.hit():
                    self._targets.remove(result)

            self._attempts -= 1

        if all(str(target) == "Obstacle" for target in self.targets):
            return True
        return False

    def draw_board(self) -> None:
        """
        Creates a pyplot figure representing the current
        state of the board.
        """

        plt.figure(figsize=(8, 4))
        plt.xlim(0, MAX_X + 1)
        plt.ylim(0, MAX_Y + 1)
        plt.xticks(range(0, MAX_X + 1, 4))
        plt.yticks(range(0, MAX_Y + 1, 2))
        fig = plt.gcf()
        ax = fig.gca()

        ax.add_patch(Bullet.draw())
        for target in self.targets:
            ax.add_patch(target.draw())

        fig.savefig('./board.png')

    def draw_trajectory(self, trajectory: List[Tuple[float, float]]) -> None:
        """
        Draws the bullets trajectory on the board.
        """

        x = [p[0] for p in trajectory]
        y = [p[1] for p in trajectory]
        plt.plot(x, y, ':', color="black")
        plt.savefig('./plot.png')
