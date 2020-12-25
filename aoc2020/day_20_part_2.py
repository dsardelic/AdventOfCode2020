import functools

from aoc2020 import day_20_part_1


def assemble_big_image(tile_layout):
    def crop_images(images):
        return tuple(
            tuple(pixel_row[1:-1] for pixel_row in image[1:-1]) for image in images
        )

    def assemble_images_horizontally(images):
        return [
            list(functools.reduce(str.__add__, (image[i] for image in images)))
            for i in range(len(images[0]))
        ]

    def assemble_images_vertically(pixel_rows):
        return functools.reduce(list.__add__, pixel_rows)

    return assemble_images_vertically(
        assemble_images_horizontally(crop_images(tile.image for tile in tile_row))
        for tile_row in tile_layout
    )


def mark_monsters(monsters, big_image):
    def encountered_monster(big_image, row_index, col_index, monster_pixel_offsets):
        return all(
            big_image[row_index + row_offset][col_index + col_offset] == "#"
            for row_offset, col_offset in monster_pixel_offsets
        )

    def mark_monster(big_image, row_index, col_index, monster_pixel_offsets):
        for row_offset, col_offset in monster_pixel_offsets:
            big_image[row_index + row_offset][col_index + col_offset] = "O"

    for monster in monsters:
        monster_pixel_offsets = tuple(
            (row_index, col_index)
            for row_index, pixel_row in enumerate(monster)
            for col_index, pixel in enumerate(pixel_row)
            if pixel == "#"
        )
        for pixel_row_index, pixel_row in enumerate(
            big_image[: len(big_image) - len(monster) + 1]
        ):
            for pixel_col_index, _ in enumerate(
                pixel_row[: len(big_image[0]) - len(monster[0]) + 1]
            ):
                if encountered_monster(
                    big_image,
                    pixel_row_index,
                    pixel_col_index,
                    monster_pixel_offsets,
                ):
                    mark_monster(
                        big_image,
                        pixel_row_index,
                        pixel_col_index,
                        monster_pixel_offsets,
                    )


def solution(input_rel_uri):
    tile_layout = day_20_part_1.resolve_tile_layout(input_rel_uri)
    big_image = assemble_big_image(tile_layout)
    monster_image_variants = tuple(
        image_variant
        for image_variant in day_20_part_1.create_image_variants(
            (
                "                  # ",  # dummy comment to prevent Black autoformatting
                "#    ##    ##    ###",
                " #  #  #  #  #  #   ",
            )
        )
    )
    mark_monsters(monster_image_variants, big_image)
    return sum(pixel == "#" for line in big_image for pixel in line)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
