from target import Target, Obstacle
from level import Level, IvalidAttemptsError
from pytest import raises


def test_level_init():
    level = Level(1, [])
    assert level.attempts == 1
    assert level.targets == []
    assert level.trajectory == []
    assert level.result is False


def test_level_init_error():
    with raises(IvalidAttemptsError):
        Level(0, [])


def test_simulate_attempt_hit():
    target = Target(32, 16)
    obstacle = Obstacle(32, 16)
    level = Level(1, [target, obstacle])
    assert level.simulate_attempt(45, 100) is target
    assert level.attempts == 0
    assert level.result is True


def test_simulate_attempt_miss():
    target = Target(32, 16)
    obstacle = Obstacle(32, 16)
    level = Level(1, [target, obstacle])
    assert level.simulate_attempt(45, 90) is obstacle
    assert level.attempts == 0
    assert level.result is False
