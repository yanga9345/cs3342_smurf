from old_rply_code.smurf_lexer import Lexer
from old_rply_code.smurf_parser import Parser

text_input = """
let a = 1
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()