from level import Level
from target import Target, Obstacle, Boss


def main():
    targets = [Obstacle(32, 16), Target(32, 16), Boss(28, 0, 2)]
    level = Level(3, targets)

    if level.play():
        print("Level Won!")
    else:
        print("Level Lost")


if __name__ == "__main__":
    main()
