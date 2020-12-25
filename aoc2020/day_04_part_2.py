import re

ALL_PASSWORD_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


def password_has_all_required_fields(password):
    missing_fields = [field for field in ALL_PASSWORD_FIELDS if field not in password]
    return not missing_fields or missing_fields == ["cid"]


def is_valid_byr(byr: str):
    if match := re.match(r"^(\d{4})$", byr):
        return 1920 <= int(match[0]) <= 2002
    return False


def is_valid_iyr(iyr: str):
    if match := re.match(r"^(\d{4})$", iyr):
        return 2010 <= int(match[0]) <= 2020
    return False


def is_valid_eyr(eyr: str):
    if match := re.match(r"^(\d{4})$", eyr):
        return 2020 <= int(match[0]) <= 2030
    return False


def is_valid_hgt(hgt: str):
    if match := re.match(r"^(\d+)(cm|in)$", hgt):
        number, unit = match.groups()
        if unit == "cm":
            return 150 <= int(number) <= 193
        return 59 <= int(number) <= 76
    return False


def is_valid_hcl(hcl: str):
    return re.match(r"^#[0-9a-f]{6}$", hcl)


def is_valid_ecl(ecl: str):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_pid(pid: str):
    return re.match(r"^\d{9}$", pid)


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        raw_passwords_data = ifile.read().rstrip().split("\n\n")
    valid_passwords_count = 0
    validators = (
        is_valid_byr,
        is_valid_iyr,
        is_valid_eyr,
        is_valid_hgt,
        is_valid_hcl,
        is_valid_ecl,
        is_valid_pid,
    )
    for raw_password_data in raw_passwords_data:
        password_kvs_strings = re.split(r"[ \n]", raw_password_data)
        password = dict(kvs_string.split(":") for kvs_string in password_kvs_strings)
        if password_has_all_required_fields(password) and all(
            validator(password[field])
            for validator, field in zip(validators, ALL_PASSWORD_FIELDS)
        ):
            valid_passwords_count += 1
    return valid_passwords_count


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
