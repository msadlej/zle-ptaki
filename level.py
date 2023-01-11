from bullet import Bullet, MAX_X, MAX_Y
from target import Target
from typing import List, Tuple
from matplotlib import pyplot as plt
from io import BytesIO
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox


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
    def result(self) -> bool:
        """
        Returns the result of the level.
        """

        return self._result

    def setup_ui(self, window, button, plot, AngleSlider, ForceSlider) -> None:
        """
        Sets up the ui for level simulation.
        """

        self.window = window
        self.button = button
        self.plot = plot
        self.AngleSlider = AngleSlider
        self.ForceSlider = ForceSlider

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
            self.plot.setPixmap(pixmap)

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
            self.plot.setPixmap(pixmap)

    def simulate_attempt(self) -> None:
        """
        Simulates the attempt.
        Draws the board and bullets trajectory.
        Waits for the angle and force input.
        Sets result to true if the level was won.
        """

        angle = self.AngleSlider.value()
        force = self.ForceSlider.value()
        bullet = Bullet(angle, force)
        attempt_result = bullet.calculate_trajectory(self.targets)
        self.draw_trajectory(bullet.trajectory)
        self._attempts -= 1

        if attempt_result is None:
            QMessageBox.information(self.plot, "QMessageBox", f"Missed! Remaining attempts: {self.attempts}")
        else:
            QMessageBox.information(self.plot, "QMessageBox", f"{attempt_result} hit! Remaining attempts: {self.attempts}")

            if attempt_result.hit():
                self._targets.remove(attempt_result)

        self.draw_board()

        if all(str(target) == "Obstacle" for target in self.targets):
            self._result = True

        if self.result:
            self.plot.setText("Level Won!")
            self.button.clicked.disconnect()
            self.button.setText("Next")
            self.button.clicked.connect(self.window.nextPage)
        elif self.attempts == 0:
            self.plot.setText("Level Lost!")
            self.button.clicked.disconnect()
            self.button.setText("Next")
            self.button.clicked.connect(self.window.exitPage)

    def play(self):
        """
        Initializes the level simulation.
        """

        self.button.clicked.disconnect()
        self.button.clicked.connect(self.simulate_attempt)
        self.button.setText("Go")
        self.draw_board()
