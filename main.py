from smurf_lexer import Lexer
from smurf_parser import Parser

text_input = """
print(2 * 5 - 3*2)
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()