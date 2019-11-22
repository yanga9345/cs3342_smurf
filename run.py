from arpeggio import ParserPython, visit_parse_tree
import visitor
import smurf_grammar


def main(debug):
    parser = ParserPython(smurf_grammar.program, debug=debug)

    f = open("test_cases/test.smu", "r")
    contents = f.read()

    parse_tree = parser.parse(contents)

    result = visit_parse_tree(parse_tree, visitor.Visitor(debug=debug))


if __name__ == "__main__":
    main(debug=True)
    #main()