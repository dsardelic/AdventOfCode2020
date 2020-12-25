def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        lines = [line.strip() for line in ifile.readlines()]
    earliest_departure = int(lines[0])
    service_ids = [int(token) for token in lines[1].split(",") if token != "x"]
    min_waiting_time, earliest_service_id = min(
        ((service_id - earliest_departure % service_id) % service_id, service_id)
        for service_id in service_ids
    )
    return min_waiting_time * earliest_service_id


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
