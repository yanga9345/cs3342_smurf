from smurf_lexer import Lexer
from smurf_parser import Parser

#f = open('test_cases/00_expr.smu', 'r')
f = open('test_cases/test.smu', 'r')
#f = open('test_cases/01_variables.smu', 'r')
contents = f.read()
lines = contents.splitlines()

lexer = Lexer().get_lexer()
pg = Parser()
pg.parse()
parser = pg.get_parser()

for line in lines:
    if len(line) > 0:
        tokens = lexer.lex(line)
        parser.parse(tokens).eval()


