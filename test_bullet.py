from bullet import Bullet, InvalidAngleError, InvalidForceError
from target import Target, Obstacle, Boss
import pytest
from math import pi
from matplotlib import pyplot as plt


def test_bullet_init():
    bullet = Bullet(45, 100)
    assert bullet.angle == pytest.approx(pi/4)
    assert bullet.force == 25
    assert bullet.trajectory == []
    assert bullet.position == (0, 0)


def test_bullet_init_angle_error():
    with pytest.raises(InvalidAngleError):
        Bullet(-1, 100)


def test_bullet_init_force_error():
    with pytest.raises(InvalidForceError):
        Bullet(45, 101)


def test_check_position():
    bullet = Bullet(45, 100)
    assert bullet.check_position() is True


def test_calculate_trajectory_empty():
    bullet = Bullet(45, 100)
    assert bullet.calculate_trajectory([]) is None


def test_calculate_trajectory_target_hit():
    bullet = Bullet(45, 100)
    target = Target(1, 1)
    assert bullet.calculate_trajectory([target]) is target


def test_calculate_trajectory_target_miss():
    bullet = Bullet(45, 100)
    target = Target(1, 0)
    assert bullet.calculate_trajectory([target]) is None


def test_calculate_trajectory_obstacle_miss():
    bullet = Bullet(45, 100)
    target = Obstacle(32, 16)
    assert bullet.calculate_trajectory([target]) is None


def test_calculate_trajectory_obstacle_target_hit():
    bullet = Bullet(45, 100)
    targets = [Obstacle(32, 16), Target(32, 16)]
    assert bullet.calculate_trajectory(targets) is targets[1]


def test_calculate_trajectory_obstacle_target_boss_hit():
    bullet = Bullet(45, 100)
    targets = [Obstacle(32, 16), Target(32, 16), Boss(1, 0, 2)]
    assert bullet.calculate_trajectory(targets) is targets[2]


def test_target_draw():
    circle = plt.Circle((0, 0), 0.5, color="red")
    assert str(Bullet.draw()) == str(circle)
