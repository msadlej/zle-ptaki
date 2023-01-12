from level import Level
from target import Target, Obstacle, Boss
from typing import List
from ui_zle_ptaki import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
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
        self.levels = []
        self.current_level = 0
        self.resetSliders()

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

        self.ui.AngleSlider.setValue(0)
        self.ui.ForceSlider.setValue(0)

    def messageBox(self, title: str, message: str) -> None:
        QMessageBox.information(self, title, message)

    def addLevel(self, attempts: int, targets: List[Target]) -> None:
        """
        Adds a level to the levels list.
        """

        level = Level(attempts, targets, self)
        self.levels.append(level)

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

        self.ui.plot.setText("Level Completed!")
        self.ui.button.setText("Next")

        self.current_level += 1
        if self.current_level == self.number_of_levels:
            self.ui.button.clicked.connect(self.gameWonPage)
            return

        self.ui.button.clicked.connect(self.startLevel)

    def startLevel(self) -> None:
        """
        Starts the current level.
        """

        level = self.levels[self.current_level]
        self.ui.plot.setText(f"Level {self.current_level + 1}\nNumber of attempts: {level.attempts}")
        self.ui.button.setText("Start")
        self.ui.button.clicked.connect(level.play)

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
        self.ui.button.setText("Exit")
        self.ui.button.clicked.connect(self.close)


def main(args):
    app = QApplication(args)
    window = ZlePtakiWindow()

    window.addLevel(1, [Target(32, 0)])
    window.addLevel(2, [Obstacle(32, 16), Target(32, 16)])
    window.addLevel(4, [Obstacle(32, 16), Target(32, 16), Boss(28, 0, 2)])

    window.startLevel()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    main(sys.argv)
