from level import Level
from target import Target, Obstacle, Boss
from ui_main import Ui_MainWindow
import sys
from PySide2.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stack.setCurrentIndex(0)
        self.number_of_levels = 2
        self.ui.button_exit.clicked.connect(self.close)

    def nextPage(self):
        current_index = self.ui.stack.currentIndex()
        self.ui.stack.setCurrentIndex(current_index + 1)

    def exitPage(self):
        self.ui.stack.setCurrentIndex(self.number_of_levels)


def main(args):
    app = QApplication(args)
    window = MainWindow()

    targets1 = [Target(32, 0)]
    level1 = Level(1, targets1)
    level1.setup_ui(window, window.ui.button_1, window.ui.plot_1, window.ui.AngleSlider_1, window.ui.ForceSlider_1)
    window.ui.button_1.clicked.connect(level1.play)

    targets2 = [Obstacle(32, 16), Target(32, 16), Boss(28, 0, 2)]
    level2 = Level(3, targets2)
    level2.setup_ui(window, window.ui.button_2, window.ui.plot_2, window.ui.AngleSlider_2, window.ui.ForceSlider_2)
    window.ui.button_2.clicked.connect(level2.play)

    window.show()
    return app.exec_()


if __name__ == "__main__":
    main(sys.argv)
