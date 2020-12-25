import re


def apply_mask(mask, value):
    def calculate_mask_values(mask):
        mask_set_zeros = mask.replace("X", "1")
        mask_set_ones = mask.replace("X", "0")
        return int(mask_set_zeros, 2), int(mask_set_ones, 2)

    mask_set_zeros, mask_set_ones = calculate_mask_values(mask)
    return (value & mask_set_zeros) | mask_set_ones


def write_to_memory(instruction, mask, memory):
    address, value = (
        int(group) for group in re.match(r"mem\[(\d+)\] = (\d+)", instruction).groups()
    )
    memory[address] = apply_mask(mask, value)


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        lines = ifile.read().strip().split("\n")
    mask, memory = None, {}
    for line in lines:
        if match := re.match(r"mask = ([X01]+)", line):
            mask = match.group(1)
        else:
            write_to_memory(line, mask, memory)
    return sum(value for _, value in memory.items())


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
