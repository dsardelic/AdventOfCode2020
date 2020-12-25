import itertools


def apply_rules(significant_space):
    def pad_space(space):
        def pad_plane(plane):
            padded_x_len = len(plane[0]) + 2
            return [
                ["." for _ in range(padded_x_len)],
                *(["."] + row + ["."] for row in plane),
                ["." for _ in range(padded_x_len)],
            ]

        padded_y_len = len(space[0]) + 2
        padded_x_len = len(space[0][0]) + 2
        return [
            [["." for _ in range(padded_x_len)] for _ in range(padded_y_len)],
            *(pad_plane(plane) for plane in space),
            [["." for _ in range(padded_x_len)] for _ in range(padded_y_len)],
        ]

    new_significant_space = pad_space(significant_space)

    padded_new_significant_space = pad_space(new_significant_space)

    def set_cube_state(curr_state, coord_z, coord_y, coord_x):
        def count_surrounding_active_cubes(coord_z, coord_y, coord_x):
            return sum(
                padded_new_significant_space[coord_z + offset_z][coord_y + offset_y][
                    coord_x + offset_x
                ]
                == "#"
                for offset_z in range(-1, 2)
                for offset_y in range(-1, 2)
                for offset_x in range(-1, 2)
                if (offset_z, offset_y, offset_x) != (0, 0, 0)
            )

        surrounding_active_cubes_count = count_surrounding_active_cubes(
            coord_z + 1,
            coord_y + 1,
            coord_x + 1,
        )
        if curr_state == "#" and surrounding_active_cubes_count not in [
            2,
            3,
        ]:
            new_significant_space[coord_z][coord_y][coord_x] = "."
        elif curr_state == "." and surrounding_active_cubes_count == 3:
            new_significant_space[coord_z][coord_y][coord_x] = "#"
        else:
            new_significant_space[coord_z][coord_y][coord_x] = curr_state

    for coord_z, plane in enumerate(new_significant_space):
        for coord_y, line in enumerate(plane):
            for coord_x, curr_state in enumerate(line):
                set_cube_state(
                    curr_state,
                    coord_z,
                    coord_y,
                    coord_x,
                )
    return new_significant_space


def solution(input_rel_uri):
    def light_up_cubes(space):
        for _ in range(6):
            space = apply_rules(space)
        return space

    with open(input_rel_uri) as ifile:
        space = [[list(line) for line in ifile.read().strip().split("\n")]]
    return sum(
        state == "#"
        for state in itertools.chain.from_iterable(
            itertools.chain.from_iterable(light_up_cubes(space))
        )
    )


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}_example.txt"))
