import sys
from arpeggio import ParserPython, visit_parse_tree
import visitor
import smurf_grammar
from interpreter import Binding


def main(debug):
    parser = ParserPython(smurf_grammar.program, smurf_grammar.comment, debug=debug)
    f = open(sys.argv[1], "r")
    contents = f.read()
    parse_tree = parser.parse(contents)

    result = visit_parse_tree(parse_tree, visitor.Visitor(debug=debug))
    global_binding = Binding(None, {})
    result.eval(global_binding)


if __name__ == "__main__":
    main(debug=False)