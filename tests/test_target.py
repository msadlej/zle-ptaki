from target import (
    Target,
    Obstacle,
    Boss,
    InvalidHealthError,
    InvalidHeightError,
    InvalidPositionError,
)
from matplotlib import pyplot as plt
from pytest import raises


def test_target_init():
    target = Target(1, 0)
    assert target._position_x == 1
    assert target._position_y == 0


def test_target_init_error_x():
    with raises(InvalidPositionError):
        Target(-1, 1)


def test_target_init_error_y():
    with raises(InvalidPositionError):
        Target(1, -1)


def test_target_position():
    target = Target(1, 0)
    assert target.position == [(1, 0)]


def test_target_hit():
    target = Target(1, 1)
    assert target.hit() is True


def test_target_draw():
    target = Target(1, 1)
    circle = plt.Circle((1, 1), 0.5, color="green")
    assert str(target.draw()) == str(circle)


def test_target_str():
    target = Target(1, 2)
    assert str(target) == "Target"


def test_obstacle_init():
    obstacle = Obstacle(1, 2)
    assert obstacle.height == 2


def test_obstacle_init_error():
    with raises(InvalidHeightError):
        Obstacle(1, 0)


def test_obstacle_position():
    obstacle = Obstacle(1, 2)
    assert obstacle.position == [(1, 0), (1, 1)]


def test_obstacle_position_one_height():
    obstacle = Obstacle(1, 1)
    assert obstacle.position == [(1, 0)]


def test_obstacle_hit():
    obstacle = Obstacle(1, 2)
    assert obstacle.hit() is False


def test_obstacle_draw():
    obstacle = Obstacle(1, 2)
    rectangle = plt.Rectangle((0.5, 0), 1, 1.5, color="saddlebrown")
    assert str(obstacle.draw()) == str(rectangle)


def test_obstacle_str():
    obstacle = Obstacle(1, 2)
    assert str(obstacle) == "Obstacle"


def test_boss_init():
    boss = Boss(1, 0, 2)
    assert boss.health == 2


def test_boss_init_error():
    with raises(InvalidHealthError):
        Boss(1, 0, -1)


def test_boss_position():
    boss = Boss(1, 0, 2)
    assert boss.position == [(1, 0), (2, 0), (1, 1), (2, 1)]


def test_boss_hit():
    boss = Boss(1, 0, 2)
    assert boss.hit() is False
    assert boss.health == 1
    assert boss.hit() is True
    assert boss.health == 0


def test_boss_draw():
    boss = Boss(1, 0, 2)
    circle = plt.Circle((1.5, 0.5), 1, color="blue")
    assert str(boss.draw()) == str(circle)


def test_boss_str():
    boss = Boss(1, 0, 2)
    assert str(boss) == "Boss"
