from rply import ParserGenerator
from ast import Number, Print, Sum, Sub, Mult, Div, Assign, Variable

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['LET', 'NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'MULT', 'DIV', 'SUM', 'SUB', 'ASSIGN', 'VAR'],
            precedence=[
                ('left', ['PRINT']),
                ('left', ['ASSIGN']),
                ('left', ['LET']),
                ('left', ['SUM', 'SUB', ]),
                ('left', ['MULT', 'DIV', ]),
                ('left', ['OPEN_PAREN', 'CLOSE_PAREN', ]),
            ]
        )

        self.variables = {}

    def parse(self):

        #@self.pg.production('statement : expression')
        #def statement_expr(state, p):
        #    return p[0]

        @self.pg.production('function : LET VAR ASSIGN expression')
        @self.pg.production('function : VAR ASSIGN expression')
        def assignment(p):
            if p[0].value == 'let':
                return Assign(p[1].value, p[3].eval(), self.variables)
            else:
                return Assign(p[0].value, p[2].eval(), self.variables)

        @self.pg.production('function : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def output(p):
            return Print(p[2])

        @self.pg.production('expression : VAR')
        def variable(p):
            return Variable(p[0].value, self.variables)

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

        @self.pg.production('expression : SUB NUMBER')
        def negative_number(p):
            return Mult(Number(p[1].value), Number(-1))

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def factor_paren(p):
            return p[1]


        #@self.pg.production('expression : LET VAR ASSIGN expression')
        # @self.pg.production('expression : var ASSIGN expression')
        #def assignment(p):
        #    return Number(p[3].value)
            # return Assign(p[1], p[3], self.variables)

    def get_parser(self):
        return self.pg.build()
