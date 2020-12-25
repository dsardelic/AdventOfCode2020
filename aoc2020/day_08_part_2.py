import re


def fix_program_and_calculate_accumulator(instructions):
    for instruction_index, (instruction, value) in enumerate(instructions):
        if instruction in ("jmp", "nop"):
            instructions_copy = [*instructions]
            if instruction == "jmp":
                instructions_copy[instruction_index] = ("nop", value)
            else:
                instructions_copy[instruction_index] = ("jmp", value)
            if accumulator := calculate_accumulator(instructions_copy):
                return accumulator
    return None


def calculate_accumulator(instructions):
    instructions_len = len(instructions)
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
        else:
            instruction_index += 1
        if instruction_index in executed_instructions:
            break
        if instruction_index == instructions_len:
            return accumulator


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
    return fix_program_and_calculate_accumulator(instructions)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
