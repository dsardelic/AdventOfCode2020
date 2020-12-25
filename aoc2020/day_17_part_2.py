import itertools


def apply_rules(significant_hyperspace):
    def pad_hyperspace(hyperspace):
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

        padded_z_len = len(hyperspace[0]) + 2
        padded_y_len = len(hyperspace[0][0]) + 2
        padded_x_len = len(hyperspace[0][0][0]) + 2
        padded_hyperspace = [
            [
                [["." for _ in range(padded_x_len)] for _ in range(padded_y_len)]
                for _ in range(padded_z_len)
            ],
            *(pad_space(space) for space in hyperspace),
            [
                [["." for _ in range(padded_x_len)] for _ in range(padded_y_len)]
                for _ in range(padded_z_len)
            ],
        ]
        return padded_hyperspace

    new_significant_hyperspace = pad_hyperspace(significant_hyperspace)

    padded_new_significant_hyperspace = pad_hyperspace(new_significant_hyperspace)

    def set_hypercube_state(coord_w, coord_z, coord_y, coord_x, curr_state):
        def count_surrounding_active_cubes(coord_w, coord_z, coord_y, coord_x):
            return sum(
                padded_new_significant_hyperspace[coord_w + offset_w][
                    coord_z + offset_z
                ][coord_y + offset_y][coord_x + offset_x]
                == "#"
                for offset_w in range(-1, 2)
                for offset_z in range(-1, 2)
                for offset_y in range(-1, 2)
                for offset_x in range(-1, 2)
                if (offset_w, offset_z, offset_y, offset_x) != (0, 0, 0, 0)
            )

        surrounding_active_cubes_count = count_surrounding_active_cubes(
            coord_w + 1,
            coord_z + 1,
            coord_y + 1,
            coord_x + 1,
        )
        if curr_state == "#" and surrounding_active_cubes_count not in [
            2,
            3,
        ]:
            new_significant_hyperspace[coord_w][coord_z][coord_y][coord_x] = "."
        elif curr_state == "." and surrounding_active_cubes_count == 3:
            new_significant_hyperspace[coord_w][coord_z][coord_y][coord_x] = "#"
        else:
            new_significant_hyperspace[coord_w][coord_z][coord_y][coord_x] = curr_state

    for coord_w, space in enumerate(new_significant_hyperspace):
        for coord_z, plane in enumerate(space):
            for coord_y, line in enumerate(plane):
                for coord_x, curr_state in enumerate(line):
                    set_hypercube_state(
                        coord_w,
                        coord_z,
                        coord_y,
                        coord_x,
                        curr_state,
                    )
    return new_significant_hyperspace


def solution(input_rel_uri):
    def light_up_hypercubes(hyperspace):
        for _ in range(6):
            hyperspace = apply_rules(hyperspace)
        return hyperspace

    with open(input_rel_uri) as ifile:
        hyperspace = [[[list(line) for line in ifile.read().strip().split("\n")]]]
    return sum(
        state == "#"
        for state in itertools.chain.from_iterable(
            itertools.chain.from_iterable(
                itertools.chain.from_iterable(light_up_hypercubes(hyperspace))
            )
        )
    )


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
