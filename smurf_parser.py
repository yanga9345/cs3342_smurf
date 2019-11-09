from rply import ParserGenerator
from ast import Number, Print, Sum, Sub, Mult, Div

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'MULT', 'DIV', 'SUM', 'SUB'],
            precedence=[
                ('left', ['PRINT']),
                ('left', ['SUM', 'SUB', ]),
                ('left', ['MULT', 'DIV', ]),
            ]
        )

    def parse(self):
        #@self.pg.production('statement : expression')
        #def statement_expr(state, p):
        #    return p[0]

        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def program(p):
            return Print(p[2])

        @self.pg.production('expression : expression MULT expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'MULT':
                return Mult(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
            elif operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
