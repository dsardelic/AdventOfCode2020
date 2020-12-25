import re
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Orientation:
    heading: str
    offset_per_heading: defaultdict

    def move_in_cardinal_direction(self, cardinal_direction, value):
        self.offset_per_heading[cardinal_direction] += value

    def turn(self, direction, degrees):
        if direction == "L":
            new_headings = {
                "N": "W",
                "E": "N",
                "S": "E",
                "W": "S",
            }
        else:
            new_headings = {
                "N": "E",
                "E": "S",
                "S": "W",
                "W": "N",
            }
        degrees %= 360
        while degrees:
            self.heading = new_headings[self.heading]
            degrees -= 90

    def move_in_current_heading(self, value):
        self.offset_per_heading[self.heading] += value

    @property
    def ship_abs_ew(self):
        return self.offset_per_heading["E"] - self.offset_per_heading["W"]

    @property
    def ship_abs_ns(self):
        return self.offset_per_heading["N"] - self.offset_per_heading["S"]

    @property
    def ship_distance(self):
        return abs(self.ship_abs_ew) + abs(self.ship_abs_ns)


def execute_instruction(action, value, orientation):
    if action in ["N", "S", "E", "W"]:
        orientation.move_in_cardinal_direction(action, value)
    elif action in ["R", "L"]:
        # assert value % 360 in [0, 90, 180, 270]
        orientation.turn(action, value)
    else:
        orientation.move_in_current_heading(value)


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        lines = ifile.read().strip().split("\n")
    regex = r"^([NSEWLRF])(\d+)$"
    instructions = (re.match(regex, line).groups() for line in lines)
    instructions = ((action, int(value)) for action, value in instructions)

    orientation = Orientation("E", defaultdict(int))
    for action, value in instructions:
        execute_instruction(action, value, orientation)

    return orientation.ship_distance


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
