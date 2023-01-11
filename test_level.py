from level import Level, IvalidAttemptsError
import pytest


def test_level_init():
    level = Level(1, [])
    assert level.attempts == 1
    assert level.targets == []


def test_level_init_error():
    with pytest.raises(IvalidAttemptsError):
        Level(0, [])
