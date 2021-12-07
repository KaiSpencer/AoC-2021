from dataclasses import dataclass


@dataclass
class Command:
    direction: str
    distance: int


class Submarine:
    def __init__(self, horizontal_position=0, depth=0, aim=0) -> None:
        self.horizontal_position = horizontal_position
        self.depth = depth
        self.aim = aim

    def get_position(self):
        return (self.horizontal_position, self.depth)

    def follow_command(self, command: Command):
        if command.direction == "up":
            self.depth -= command.distance
        elif command.direction == "down":
            self.depth += command.distance
        else:
            self.horizontal_position += command.distance

    def follow_command_part_2(self, command: Command):
        if command.direction == "up":
            self.aim -= command.distance
        elif command.direction == "down":
            self.aim += command.distance
        else:
            self.horizontal_position += command.distance
            self.depth += self.aim * command.distance


def main():
    submarine = Submarine()
    commands = get_test_data()
    for command in commands:
        submarine.follow_command(command)
    horizontal, depth = submarine.get_position()
    print("part 1: " + horizontal * depth)

    submarine_2 = Submarine()
    commands = get_test_data()
    for command in commands:
        submarine_2.follow_command_part_2(command)
    horizontal, depth = submarine.get_position()
    print("part 2: " + horizontal * depth)


def get_test_data():
    lines = open("testdata.txt").readlines()
    return [
        Command(direction=line.split()[0], distance=(int(line.split()[1])))
        for line in lines
    ]


if __name__ == "__main__":
    main()
