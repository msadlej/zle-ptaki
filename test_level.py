from level import Level, IvalidAttemptsError
from PySide2.QtWidgets import QMainWindow
import pytest


def test_level_init():
    window = QMainWindow()
    level = Level(1, [], window)
    assert level.attempts == 1
    assert level.targets == []
    assert level.result is False
    assert level.window is window


def test_level_init_error():
    with pytest.raises(IvalidAttemptsError):
        Level(0, [], QMainWindow())
