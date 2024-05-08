from lib.target import Target, Obstacle, Boss
from lib.level import Level
from typing import List
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtGui import QPixmap
from lib.ui_zle_ptaki import Ui_MainWindow
import sys


class ZlePtakiWindow(QMainWindow):
    """
    Class ZlePtakiWindow. Contains attributes:
    :param levels: List of levels
    :param type: List[Level]

    :param current_level: Number of the current level
    :param type: int
    """

    def __init__(self, parent=None) -> None:
        """
        Creates an instance of class ZlePtakiWindow.
        """

        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resetSliders()
        self.ui.AngleSlider.valueChanged.connect(self.updateAngleSpinBox)
        self.ui.ForceSlider.valueChanged.connect(self.updateForceSpinBox)
        self._levels = []
        self._current_level = 0

    @property
    def levels(self) -> List[Level]:
        """
        Returns the list of levels.
        """

        return self._levels

    @property
    def current_level(self) -> int:
        """
        Returns the number of the current level.
        """

        return self._current_level

    @property
    def number_of_levels(self) -> int:
        """
        Returns the current number of levels
        """

        return len(self.levels)

    def resetSliders(self) -> None:
        """
        Resets the sliders to starting positions.
        """

        self.ui.AngleSlider.setValue(1)
        self.ui.ForceSlider.setValue(1)
        self.updateAngleSpinBox()
        self.updateForceSpinBox()

    def updateAngleSpinBox(self) -> None:
        """
        Updates the Angle spinBox value.
        """

        self.ui.AngleSpinBox.setValue(self.ui.AngleSlider.value())

    def updateForceSpinBox(self) -> None:
        """
        Updates the Force spinBox value.
        """

        self.ui.ForceSpinBox.setValue(self.ui.ForceSlider.value())

    def setPlot(self, buffer) -> None:
        """
        Sets the plot to given image.
        """

        image_data = buffer.getvalue()
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.ui.plot.setPixmap(pixmap)

    def addLevel(self, attempts: int, targets: List[Target]) -> None:
        """
        Adds a level to the levels list.
        """

        level = Level(attempts, targets)
        self._levels.append(level)

    def gameWonPage(self) -> None:
        """
        Creates a page informing the player, that he won the game.
        """

        self.ui.plot.setText("Congratulations!\nYou have won the game!")
        self.ui.button.setText("Exit")
        self.ui.button.clicked.connect(self.close)

    def gameOverPage(self) -> None:
        """
        Creates a page informing the player, that he lost the game.
        """

        self.ui.plot.setText("Game Over!")
        self.ui.button.setText("Try again")
        self.ui.button.clicked.connect(self.startGame)

    def nextLevel(self) -> None:
        """
        Changes the level to the next on the list.
        Checks if last level was won.
        Checks if the player completed all levels.
        """

        level = self.levels[self.current_level]
        if not level.result:
            self.gameOverPage()
            return

        self._current_level += 1
        if self.current_level == self.number_of_levels:
            self.gameWonPage()
            return

        self.ui.plot.setText("Level Completed!")
        self.ui.button.setText("Next")
        self.ui.button.clicked.connect(self.startLevel)

    def startAttempt(self) -> None:
        """
        Starts the attempt.
        """

        level = self.levels[self.current_level]
        angle = self.ui.AngleSlider.value()
        force = self.ui.ForceSlider.value()
        attempt_result = level.simulate_attempt(angle, force)

        self.setPlot(level.draw_trajectory())
        if attempt_result is None:
            QMessageBox.information(
                self, "Attempt info", f"Missed!\nRemaining attempts: {level.attempts}"
            )
        else:
            QMessageBox.information(
                self,
                "Attempt info",
                f"{attempt_result} hit!\nRemaining attempts: {level.attempts}",
            )

        self.setPlot(level.draw_board())
        self.resetSliders()
        if level.result or level.attempts == 0:
            self.ui.button.clicked.disconnect()
            self.nextLevel()

    def startLevel(self) -> None:
        """
        Starts the current level.
        """

        level = self.levels[self.current_level]
        self.ui.button.clicked.disconnect()
        self.ui.button.setText("Go")
        self.resetSliders()
        self.setPlot(level.draw_board())
        QMessageBox.information(
            self,
            f"Level {self.current_level + 1}",
            f"Number of attempts: {level.attempts}",
        )
        self.ui.button.clicked.connect(self.startAttempt)

    def startGame(self) -> None:
        """
        Starts the game.
        """

        self._current_level = 0
        self.ui.plot.setText("Welcome to Zle Ptaki!")
        self.ui.button.setText("Start")
        self.ui.button.clicked.connect(self.startLevel)


def main(args):
    app = QApplication(args)
    window = ZlePtakiWindow()

    window.addLevel(2, [Target(32, 0)])
    window.addLevel(3, [Obstacle(32, 16), Target(32, 16)])
    window.addLevel(4, [Obstacle(16, 8), Target(16, 8), Target(32, 0)])
    window.addLevel(5, [Boss(16, 0, 2), Obstacle(8, 15), Target(8, 15)])
    window.addLevel(
        6, [Obstacle(32, 16), Target(32, 16), Obstacle(8, 4), Boss(16, 0, 3)]
    )

    window.startGame()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    main(sys.argv)
