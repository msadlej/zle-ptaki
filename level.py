from bullet import Bullet, MAX_X, MAX_Y
from target import Target
from typing import List, Tuple
from matplotlib import pyplot as plt
from PySide2.QtGui import QPixmap
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

    :param window: UI window
    :param type: ZlePtakiWindow
    """

    def __init__(self, attempts: int, targets: List[Target], window) -> None:
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
        self._result = False
        self.window = window

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
    def result(self) -> bool:
        """
        Returns the result of the level.
        """

        return self._result

    def draw_board(self) -> None:
        """
        Creates a pyplot figure representing the current
        state of the board.
        """

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
        image_data = buffer.getvalue()
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.window.ui.plot.setPixmap(pixmap)

    def draw_trajectory(self, trajectory: List[Tuple[float, float]]) -> None:
        """
        Draws the bullets trajectory on the board.
        """

        x = [p[0] for p in trajectory]
        y = [p[1] for p in trajectory]
        plt.plot(x, y, ':', color="black")

        buffer = BytesIO()
        plt.savefig(buffer)
        image_data = buffer.getvalue()
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.window.ui.plot.setPixmap(pixmap)

    def simulate_attempt(self) -> None:
        """
        Simulates the attempt.
        Draws the board and bullets trajectory.
        Waits for the angle and force input.
        Sets result to true if the level was won.
        """

        angle = self.window.ui.AngleSlider.value()
        force = self.window.ui.ForceSlider.value()
        bullet = Bullet(angle, force)
        attempt_result = bullet.calculate_trajectory(self.targets)
        self.draw_trajectory(bullet.trajectory)
        self._attempts -= 1

        if attempt_result is None:
            self.window.messageBox("Attempt info", f"Missed!\nRemaining attempts: {self.attempts}")
        else:
            self.window.messageBox("Attempt info", f"{attempt_result} hit!\nRemaining attempts: {self.attempts}")

            if attempt_result.hit():
                self._targets.remove(attempt_result)
        self.draw_board()
        self.window.resetSliders()

        if all(str(target) == "Obstacle" for target in self.targets):
            self._result = True

        if self.result or self.attempts == 0:
            self.window.ui.button.clicked.disconnect()
            self.window.nextLevel()

    def play(self):
        """
        Initializes the level simulation.
        Draws the starting board.
        Sets up the UI.
        """

        self.window.ui.button.clicked.disconnect()
        self.window.ui.button.clicked.connect(self.simulate_attempt)
        self.window.ui.button.setText("Go")
        self.window.resetSliders()
        self.draw_board()
