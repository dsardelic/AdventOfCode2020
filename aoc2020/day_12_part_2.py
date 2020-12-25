import re
from dataclasses import dataclass


@dataclass
class Orientation:
    ship_abs_ew: int
    ship_abs_ns: int
    waypoint_rel_ew: int
    waypoint_rel_ns: int

    def move_waypoint(self, action, value):
        if action == "N":
            self.waypoint_rel_ns += value
        elif action == "S":
            self.waypoint_rel_ns -= value
        elif action == "E":
            self.waypoint_rel_ew += value
        elif action == "W":
            self.waypoint_rel_ew -= value

    def rotate_waypoint(self, direction, degrees):
        degrees %= 360
        while degrees:
            if direction == "L":
                self.waypoint_rel_ew, self.waypoint_rel_ns = (
                    -self.waypoint_rel_ns,
                    self.waypoint_rel_ew,
                )
            else:
                self.waypoint_rel_ew, self.waypoint_rel_ns = (
                    self.waypoint_rel_ns,
                    -self.waypoint_rel_ew,
                )
            degrees -= 90

    def move_ship_forward(self, value):
        self.ship_abs_ew += self.waypoint_rel_ew * value
        self.ship_abs_ns += self.waypoint_rel_ns * value

    def ship_distance(self):
        return abs(self.ship_abs_ew) + abs(self.ship_abs_ns)


def execute_instruction(action, value, orientation):
    if action in ("N", "S", "E", "W"):
        orientation.move_waypoint(action, value)
    elif action in ("L", "R"):
        orientation.rotate_waypoint(action, value)
    else:
        orientation.move_ship_forward(value)


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        lines = ifile.read().strip().split("\n")
    regex = r"^([NSEWLRF])(\d+)$"
    instructions = (re.match(regex, line).groups() for line in lines)
    instructions = ((action, int(value)) for action, value in instructions)

    orientation = Orientation(0, 0, 10, 1)
    for action, value in instructions:
        execute_instruction(action, value, orientation)
    return orientation.ship_distance()


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
