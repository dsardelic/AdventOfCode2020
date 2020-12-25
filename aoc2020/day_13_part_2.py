import functools


def slow_iterative_solution(service_offsets):
    mins_since_last_departures = [
        (service_id, (service_id - offset) % service_id)
        for service_id, offset in service_offsets
    ]
    timestamp = service_offsets[0][0]
    while not all(
        timestamp % service_id == minutes
        for service_id, minutes in mins_since_last_departures[1:]
    ):
        timestamp += service_offsets[0][0]
    return timestamp


def fast_solution_using_congruence(service_offsets):
    def solve_linear_congruence_equations(rests, modulos):
        """Taken over with respect and gratitude and modified from
        https://martin-thoma.com/solve-linear-congruence-equations/"""

        def extended_euclidean_algorithm(a, b):
            aO, bO = a, b

            x = lasty = 0
            y = lastx = 1
            while b != 0:
                q = a // b
                a, b = b, a % b
                x, lastx = lastx - q * x, x
                y, lasty = lasty - q * y, y

            return {"x": lastx, "y": lasty, "gcd": aO * lastx + bO * lasty}

        x = 0
        M = functools.reduce(lambda x, y: x * y, modulos)

        for mi, resti in zip(modulos, rests):
            Mi = M // mi
            s = extended_euclidean_algorithm(Mi, mi)["x"]
            e = s * Mi
            x += resti * e
        # return {"congruence class": ((x % M) + M) % M, "modulo": M}
        return ((x % M) + M) % M

    rests = [
        (service_id - offset) % service_id for service_id, offset in service_offsets
    ]
    modulos = [service_id for service_id, _ in service_offsets]
    return solve_linear_congruence_equations(rests, modulos)


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        lines = [line.strip() for line in ifile.readlines()]
    service_offsets = [
        (int(token), offset)
        for offset, token in enumerate(lines[1].split(","))
        if token != "x"
    ]
    # return slow_iterative_solution(service_offsets)
    return fast_solution_using_congruence(service_offsets)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
