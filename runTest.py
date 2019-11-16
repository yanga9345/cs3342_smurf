from smurf_lexer import Lexer
from smurf_parser import Parser

f = open('test_cases/00_expr.smu', 'r')
contents = f.read()
lines = contents.splitlines()

lexer = Lexer().get_lexer()
pg = Parser()
pg.parse()
parser = pg.get_parser()

for line in lines:
    tokens = lexer.lex(line)
    parser.parse(tokens).eval()


