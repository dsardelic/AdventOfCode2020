import dataclasses
import functools
import math
import re


@dataclasses.dataclass(frozen=True)
class TileVariant:
    id_: int
    image: list

    @functools.cached_property
    def left_border(self):
        return "".join(self.image[i][0] for i in range(len(self.image)))

    @functools.cached_property
    def top_border(self):
        return self.image[0]

    @functools.cached_property
    def right_border(self):
        return "".join(
            self.image[i][len(self.image[0]) - 1] for i in range(len(self.image))
        )

    @functools.cached_property
    def bottom_border(self):
        return self.image[len(self.image) - 1]


def create_image_variants(image):
    def flip_image_vertically(image):
        return image[::-1]

    def flip_image_horizontally(image):
        return tuple(content_row[::-1] for content_row in image)

    def right_rotate_image(image):
        return tuple(
            "".join(char_row[char_index] for char_row in image[::-1])
            for char_index in range(len(image[0]))
        )

    # btw every horizontal flip rotation can be achieved by rotating the vertical flip
    image_variants = []
    for base_image in [
        image,
        flip_image_vertically(image),
        flip_image_horizontally(image),
    ]:
        image_variants.append(base_image)
        for _ in range(3):
            base_image = right_rotate_image(base_image)
            image_variants.append(base_image)
    return tuple(set(image_variants))


def resolve_tile_layout(input_rel_uri):
    def create_tile_variants(tile_id, base_image):
        return tuple(
            TileVariant(tile_id, image) for image in create_image_variants(base_image)
        )

    def fill_tile_layout(tile_layout, remaining_tiles, tile_variants_per_id):
        filled_layout = None

        def fill_coordinates(row_index, col_index, tile_layout, remaining_tiles):
            def fitting_tile_variants(remaining_tiles, top_border, left_border):
                return tuple(
                    tile
                    for tile_id in remaining_tiles
                    for tile in tile_variants_per_id[tile_id]
                    if (top_border is None or tile.top_border == top_border)
                    and (left_border is None or tile.left_border == left_border)
                )

            nonlocal filled_layout

            if row_index:
                top_border = tile_layout[row_index - 1][col_index].bottom_border
            else:
                top_border = None
            if col_index:
                left_border = tile_layout[row_index][col_index - 1].right_border
            else:
                left_border = None
            for fitting_tile_variant in fitting_tile_variants(
                remaining_tiles, top_border, left_border
            ):
                if filled_layout:
                    return
                new_tile_layout = [row[:] for row in tile_layout]
                new_tile_layout[row_index][col_index] = fitting_tile_variant
                if col_index == len(tile_layout[0]) - 1:
                    new_col_index = 0
                    new_row_index = row_index + 1
                else:
                    new_col_index = col_index + 1
                    new_row_index = row_index
                if new_row_index == len(tile_layout):
                    filled_layout = new_tile_layout
                    return
                new_remaining_tiles = remaining_tiles[:]
                new_remaining_tiles.remove(fitting_tile_variant.id_)
                fill_coordinates(
                    new_row_index,
                    new_col_index,
                    new_tile_layout,
                    new_remaining_tiles,
                )

        fill_coordinates(0, 0, tile_layout, remaining_tiles)
        return filled_layout

    with open(input_rel_uri) as ifile:
        tiles_data = ifile.read().strip().split("\n\n")
    tile_variants_per_id = {}
    for tile_data in tiles_data:
        lines = tile_data.split("\n")
        tile_id = int(re.search(r"(\d+)", lines[0]).group(1))
        tile_image = tuple(lines[1:])
        tile_variants_per_id[tile_id] = create_tile_variants(tile_id, tile_image)

    tile_layout_size = int(math.sqrt(len(tile_variants_per_id.keys())))
    tile_layout = [
        [None for _ in range(tile_layout_size)] for _ in range(tile_layout_size)
    ]
    return fill_tile_layout(
        tile_layout, list(tile_variants_per_id.keys()), tile_variants_per_id
    )


def solution(input_rel_uri):
    tile_layout = resolve_tile_layout(input_rel_uri)
    return (
        tile_layout[0][0].id_
        * tile_layout[0][-1].id_
        * tile_layout[-1][0].id_
        * tile_layout[-1][-1].id_
    )


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
