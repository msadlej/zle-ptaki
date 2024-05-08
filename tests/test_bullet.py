from lib.bullet import Bullet, InvalidAngleError, InvalidForceError
from lib.target import Target, Obstacle, Boss
from matplotlib import pyplot as plt
from math import pi
from pytest import raises, approx


def test_bullet_init():
    bullet = Bullet(45, 100)
    assert bullet.angle == approx(pi / 4)
    assert bullet.force == 25
    assert bullet.trajectory == []
    assert bullet.position == (0, 0)


def test_bullet_init_angle_error():
    with raises(InvalidAngleError):
        Bullet(-1, 100)


def test_bullet_init_force_error():
    with raises(InvalidForceError):
        Bullet(45, 101)


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


def test_calculate_trajectory_obstacle_hit():
    bullet = Bullet(45, 96)
    obstacle = Obstacle(32, 16)
    assert bullet.calculate_trajectory([obstacle]) is obstacle


def test_calculate_trajectory_obstacle_miss():
    bullet = Bullet(45, 100)
    obstacle = Obstacle(32, 16)
    assert bullet.calculate_trajectory([obstacle]) is None


def test_calculate_trajectory_obstacle_target_hit():
    bullet = Bullet(45, 100)
    targets = [Obstacle(32, 16), Target(32, 16)]
    assert bullet.calculate_trajectory(targets) is targets[1]


def test_calculate_trajectory_obstacle_target_miss():
    bullet = Bullet(45, 69)
    targets = [Obstacle(32, 16), Target(32, 16)]
    assert bullet.calculate_trajectory(targets) is None


def test_calculate_trajectory_obstacle_target_boss_hit():
    bullet = Bullet(45, 69)
    targets = [Obstacle(32, 16), Target(32, 16), Boss(28, 0, 2)]
    assert bullet.calculate_trajectory(targets) is targets[2]


def test_calculate_trajectory_obstacle_target_boss_miss():
    bullet = Bullet(45, 50)
    targets = [Obstacle(32, 16), Target(32, 16), Boss(28, 0, 2)]
    assert bullet.calculate_trajectory(targets) is None


def test_calculate_trajectory_multiple():
    bullet = Bullet(45, 71)
    targets = [Target(32, 0), Obstacle(16, 8), Target(16, 8)]
    assert bullet.calculate_trajectory(targets) is targets[2]
    targets = [Target(32, 0), Obstacle(16, 8)]
    assert bullet.calculate_trajectory(targets) is targets[0]


def test_bullet_draw():
    circle = plt.Circle((0, 0), 0.5, color="red")
    assert str(Bullet.draw()) == str(circle)
