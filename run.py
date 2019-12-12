import sys
from arpeggio import ParserPython, visit_parse_tree
import visitor
import smurf_grammar
from interpreter import Binding
# NOTE: to run all tests, navigate to test_cases/ and run "run_tests.bat"


# takes in a file from argv, parses it, builds an AST, and interprets it
def main(debug):
    parser = ParserPython(smurf_grammar.program, smurf_grammar.comment, debug=debug)
    f = open(sys.argv[1], "r")
    contents = f.read()
    parse_tree = parser.parse(contents)

    result = visit_parse_tree(parse_tree, visitor.Visitor(debug=debug))
    # creates global binding without a parent
    global_binding = Binding(None, {})
    result.eval(global_binding)


if __name__ == "__main__":
    main(debug=False)
