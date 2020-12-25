import itertools
import re


def decode_mask(address, mask):
    return "".join(
        mask_bit if mask_bit in ["X", "1"] else address_bit
        for address_bit, mask_bit in zip(f"{address:036b}", mask)
    )


def get_decoded_addresses(decoded_mask):
    decoded_addresses = set()
    x_indices = [index for index, bit in enumerate(decoded_mask) if bit == "X"]
    for product in itertools.product("01", repeat=len(x_indices)):
        address_bit_strs = list(decoded_mask)
        for index, bit in zip(x_indices, product):
            address_bit_strs[index] = bit
        decoded_addresses.add(int("".join(address_bit_strs), 2))
    return decoded_addresses


def execute_instruction(instruction, mask, memory):
    if match := re.match(r"mask = ([X01]+)", instruction):
        return match.group(1), memory
    instruction_address, value = (
        int(group) for group in re.match(r"mem\[(\d+)\] = (\d+)", instruction).groups()
    )
    memory.update(
        {
            address: value
            for address in get_decoded_addresses(decode_mask(instruction_address, mask))
        }
    )
    return mask, memory


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        lines = ifile.read().strip().split("\n")
    mask, memory = None, {}
    for line in lines:
        mask, memory = execute_instruction(line, mask, memory)
    return sum(value for _, value in memory.items())


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
