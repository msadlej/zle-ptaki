from level import Level, IvalidAttemptsError
from pytest import raises


def test_level_init():
    level = Level(1, [], "window")
    assert level.attempts == 1
    assert level.targets == []
    assert level.result is False
    assert level.window == "window"


def test_level_init_error():
    with raises(IvalidAttemptsError):
        Level(0, [], "window")
