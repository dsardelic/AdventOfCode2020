import re


def solution(input_rel_uri):
    regex = r"^(acc|jmp|nop) ([+-])(\d+)$"
    with open(input_rel_uri) as ifile:
        instruction_lines = ifile.readlines()
    instructions = [
        re.match(regex, line.strip()).groups() for line in instruction_lines
    ]
    instructions = [
        (instruction, int(sign + value)) for instruction, sign, value in instructions
    ]

    accumulator = 0
    instruction_index = 0
    executed_instructions = set()
    while True:
        executed_instructions.add(instruction_index)
        instruction, value = instructions[instruction_index]
        if instruction == "acc":
            accumulator += value
            instruction_index += 1
        elif instruction == "jmp":
            instruction_index += value
            assert instruction_index >= 0
        else:
            instruction_index += 1
        if instruction_index in executed_instructions:
            return accumulator


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
