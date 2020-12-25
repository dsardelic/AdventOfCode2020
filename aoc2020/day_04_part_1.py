import re


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        raw_passwords_data = (ifile.read().rstrip()).split("\n\n")
    all_password_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    valid_passwords_count = 0
    for raw_password_data in raw_passwords_data:
        password_kvs = re.split(r"[ \n]", raw_password_data)
        password_fields = {kv.split(":")[0] for kv in password_kvs}
        missing_fields = all_password_fields.difference(password_fields)
        if not missing_fields or missing_fields == {"cid"}:
            valid_passwords_count += 1
    return valid_passwords_count


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
