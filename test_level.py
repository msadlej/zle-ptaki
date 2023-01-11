from level import Level, IvalidAttemptsError
import pytest


def test_level_init():
    level = Level(1, [])
    assert level.attempts == 1
    assert level.targets == []
    assert level.result is False


def test_level_init_error():
    with pytest.raises(IvalidAttemptsError):
        Level(0, [])
