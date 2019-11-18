from sys import argv

from smurf_lexer import Lexer
from smurf_parser import Parser

def evaluate_children(value):
    if isinstance(value, tuple):
        for element in value:
            evaluate_children(element)
    else:
        value.eval()

#with open(argv[1], 'r') as f:
#    source = f.read()

f = open('test_cases/00_expr.smu', 'r')
#f = open('test_cases/test.smu', 'r')
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
        data = parser.parse(tokens)
        #parser.parse(tokens).eval()
        evaluate_children(data)
        #data.eval()
        #parseList = parser.parse(tokens)
        #parseList.eval()
        #for x in parseList:
        #    x.eval()
#contents = "let a = 1 print(a)"
#tokens = lexer.lex(contents)
#parser.parse(tokens).eval()
