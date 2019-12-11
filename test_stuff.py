import sys
from arpeggio import ParserPython, visit_parse_tree
import visitor
import smurf_grammar


def main(debug):
    tests = [
        # "test_cases/test.smu",
        "test_cases/00_expr.smu",
        # "test_cases/01_variables.smu",
        # "test_cases/02_let.smu",
        # "test_cases/10_if.smu",
        # "test_cases/20_fn_basic.smu",
        # "test_cases/21_recursive_fns.smu",
        # "test_cases/22_closures.smu",
        # "test_cases/99_fib.smu",
    ]

    parser = ParserPython(smurf_grammar.program, smurf_grammar.comment, debug=debug)

    for file in tests:
        f = open(file, "r")
        contents = f.read()

        parse_tree = parser.parse(contents)

        result = visit_parse_tree(parse_tree, visitor.Visitor(debug=debug))
        binding = {}
        result.eval(binding)

if __name__ == "__main__":
    main(debug=False)