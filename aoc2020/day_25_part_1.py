DEFAULT_INITIAL_VALUE = 1
DEFAULT_SUBJECT_NUMBER = 7
DIVISOR = 20201227


class InvalidPublicKeyException(Exception):
    pass


def get_encryption_key_params(public_key_1, public_key_2):
    value = DEFAULT_INITIAL_VALUE
    for loop_size in range(1, DIVISOR + 1):
        value *= DEFAULT_SUBJECT_NUMBER
        value %= DIVISOR
        if value == public_key_1:
            return public_key_2, loop_size
        if value == public_key_2:
            return public_key_1, loop_size
    raise InvalidPublicKeyException()


def calculate_encryption_key(public_key, loop_size):
    value = DEFAULT_INITIAL_VALUE
    for _ in range(1, loop_size + 1):
        value *= public_key
        value %= DIVISOR
    return value


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        public_keys = (int(key) for key in ifile.read().strip().split("\n"))
    return calculate_encryption_key(*get_encryption_key_params(*public_keys))


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
