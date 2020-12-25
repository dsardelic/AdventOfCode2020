import collections
import functools
import re


def parse_directions(tile_identifier):
    regex = r"[ns][ew]|[ew]"
    return [match.group(0) for match in re.finditer(regex, tile_identifier)]


def get_tile_coordinates(tile_identifier):
    offset_xy_per_direction = {
        "e": (2, 0),
        "se": (1, -1),
        "sw": (-1, -1),
        "w": (-2, 0),
        "nw": (-1, 1),
        "ne": (1, 1),
    }
    return functools.reduce(
        lambda t1, t2: (t1[0] + t2[0], t1[1] + t2[1]),
        (
            offset_xy_per_direction[direction]
            for direction in parse_directions(tile_identifier)
        ),
    )


def flip_tiles(tile_identifiers, is_black_tile_per_coords):
    for tile_identifier in tile_identifiers:
        tile_coordinates = get_tile_coordinates(tile_identifier)
        is_black_tile_per_coords[tile_coordinates] = not is_black_tile_per_coords[
            tile_coordinates
        ]


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        tile_identifiers = [line.strip() for line in ifile.readlines()]
    is_black_tile_per_coords = collections.defaultdict(bool)
    flip_tiles(tile_identifiers, is_black_tile_per_coords)
    return sum(is_black_tile_per_coords.values())


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
