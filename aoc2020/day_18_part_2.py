import functools
import re


def solve_equation(equation):
    def solve_equation_without_parenthesis(equation):
        def resolve_additions(equation):
            while match := re.search(r"(\d+) \+ (\d+)", equation):
                equation_chars = list(equation)
                equation_chars[match.start() : match.end()] = str(
                    int(match.group(1)) + int(match.group(2))
                )
                equation = "".join(equation_chars)
            return equation

        equation = resolve_additions(equation)
        return functools.reduce(
            int.__mul__,
            (int(token) for token in equation.split(" ") if token != "*"),
            1,
        )

    def resolve_parentheses(equation):
        innermost_parentheses_regex = r"\((?!\()[0-9+* ]+\)"
        while match := re.search(innermost_parentheses_regex, equation):
            equation_chars = list(equation)
            equation_chars[match.start() : match.end()] = str(
                solve_equation_without_parenthesis(
                    equation[match.start() + 1 : match.end() - 1]
                )
            )
            equation = "".join(equation_chars)
        return equation

    return solve_equation_without_parenthesis(resolve_parentheses(equation))


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        equations = ifile.read().strip().split("\n")
    return sum(solve_equation(equation) for equation in equations)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
