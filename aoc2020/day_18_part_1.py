import re


def solve_equation(equation):
    def solve_equation_without_parenthesis(equation):
        tokens = equation.split(" ")
        result = int(tokens[0])
        for token in tokens[1:]:
            if token in ["+", "*"]:
                operation = token
            elif operation == "+":
                result += int(token)
            else:
                result *= int(token)
        return result

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
