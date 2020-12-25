import collections
import functools
import re

offset_xy_per_direction = {
    "e": (2, 0),
    "se": (1, -1),
    "sw": (-1, -1),
    "w": (-2, 0),
    "nw": (-1, 1),
    "ne": (1, 1),
}

Viewpoint = collections.namedtuple("Viewpoint", ["min_x", "max_x", "min_y", "max_y"])


def get_padded_viewpoint(is_black_tile_per_coords):
    return Viewpoint(
        min(coords[0] for coords in is_black_tile_per_coords) - 1,
        max(coords[0] for coords in is_black_tile_per_coords) + 1,
        min(coords[1] for coords in is_black_tile_per_coords) - 1,
        max(coords[1] for coords in is_black_tile_per_coords) + 1,
    )


def count_neighboring_black_tiles(pos_x, pos_y, is_black_tile_per_coords):
    return sum(
        is_black_tile_per_coords[(pos_x + offset_x, pos_y + offset_y)]
        for offset_x, offset_y in offset_xy_per_direction.values()
    )


def adjust_padded_min_max_x(pos_y, padded_min_x, padded_max_x):
    if pos_y % 2:
        if not padded_min_x % 2:
            padded_min_x -= 1
        if not padded_max_x % 2:
            padded_max_x += 1
    else:
        if padded_min_x % 2:
            padded_min_x -= 1
        if padded_max_x % 2:
            padded_max_x += 1
    return padded_min_x, padded_max_x


def do_another_day(black_tiles_cordss, is_black_tile_per_coords):
    viewpoint = get_padded_viewpoint(black_tiles_cordss)
    flip_to_black, flip_to_white = [], []
    for pos_y in range(viewpoint.min_y, viewpoint.max_y + 1):
        padded_min_x, padded_max_x = adjust_padded_min_max_x(
            pos_y, viewpoint.min_x, viewpoint.max_x
        )
        for pos_x in range(padded_min_x, padded_max_x + 1, 2):
            neighboring_black_tiles_count = count_neighboring_black_tiles(
                pos_x, pos_y, is_black_tile_per_coords
            )
            if is_black_tile_per_coords[(pos_x, pos_y)]:
                if (
                    not neighboring_black_tiles_count
                    or neighboring_black_tiles_count > 2
                ):
                    flip_to_white.append((pos_x, pos_y))
            elif neighboring_black_tiles_count == 2:
                flip_to_black.append((pos_x, pos_y))
    black_tiles_cordss[:] = [
        coords for coords in black_tiles_cordss if coords not in flip_to_white
    ] + flip_to_black
    for coords in flip_to_black:
        is_black_tile_per_coords[coords] = True
    for coords in flip_to_white:
        is_black_tile_per_coords[coords] = False


def parse_directions(tile_identifier):
    regex = r"[ns][ew]|[ew]"
    return [match.group(0) for match in re.finditer(regex, tile_identifier)]


def get_tile_coords(tile_identifier):
    return functools.reduce(
        lambda t1, t2: (t1[0] + t2[0], t1[1] + t2[1]),
        (
            offset_xy_per_direction[direction]
            for direction in parse_directions(tile_identifier)
        ),
    )


def prepare_initial_exhibit(input_rel_uri):
    with open(input_rel_uri) as ifile:
        tile_identifiers = [line.strip() for line in ifile.readlines()]
    is_black_tile_per_coords = collections.defaultdict(bool)
    for tile_identifier in tile_identifiers:
        tile_coords = get_tile_coords(tile_identifier)
        is_black_tile_per_coords[tile_coords] = not is_black_tile_per_coords[
            tile_coords
        ]
    black_tiles_cordss = [
        coords
        for coords, is_black_tile in is_black_tile_per_coords.items()
        if is_black_tile
    ]
    return black_tiles_cordss, is_black_tile_per_coords


def solution(input_rel_uri):
    black_tiles_cordss, is_black_tile_per_coords = prepare_initial_exhibit(
        input_rel_uri
    )
    for _ in range(1, 100 + 1):
        do_another_day(black_tiles_cordss, is_black_tile_per_coords)
    return len(black_tiles_cordss)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
