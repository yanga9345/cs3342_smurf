from rply import ParserGenerator
from old_rply_code.ast import Number, Print, Sum, Sub, Mult, Div, Assign, Variable


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['LET', 'NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'MULT', 'DIV', 'SUM', 'SUB', 'ASSIGN', 'VAR', 'COMMA', 'NEWLINE'],
            precedence=[
                ('left', ['COMMA']),
                ('left', ['PRINT']),
                ('left', ['ASSIGN']),
                ('left', ['LET']),
                ('left', ['SUM', 'SUB', ]),
                ('left', ['MULT', 'DIV', ]),
                ('left', ['OPEN_PAREN', 'CLOSE_PAREN', ]),
            ]
        )

        self.binding = {}

    def parse(self):
        #grammar rules:

        #@self.pg.production('program : code EOF')
        #@self.pg.production('code : statement*')
        #@self.pg.production('statement : LET variable_declaration | assignment | expr')
        #@self.pg.production('variable_declaration : decl (COMMA decl)*')
        #@self.pg.production('decl : identifier (ASSIGN expr)?')
        #@self.pg.production('identifier : [a-z][a-zA-Z_0-9]*') # prob add to lexer
        ##@self.pg.production('variable_reference : identifier')
        #@self.pg.production('if_expression : expr brace_block ( "else" brace_block )?')
        #@self.pg.production('assignment : identifier ASSIGN expr')
        ##@self.pg.production('expr : "fn" function_definition | "if" if_expression | boolean_expression | arithmetic expression')
        #@self.pg.production('mult_term : primary mulop mult_term | primary')
        #@self.pg.production('primary : integer | function_call | variable_reference | "(" arithmetic_expression ")"')
        #@self.pg.production('integer : "-"? [0-9]+')
        #@self.pg.production('addop : ADD | SUB')
        #@self.pg.production('mulop : MULT | DIV')
        #@self.pg.production('relop : "==" | "!=" | ">=" | ">" | "<=" | "<"')
        #@self.pg.production('function_call : variable_reference "(" call_arguments ")" | "print" "(" call_arguments ")"')
        #@self.pg.production('call_arguments : (expr ("," expr)*)?')
        #@self.pg.production('function_definition : param_list brace_block')
        #@self.pg.production('param_list :  "(" identifier ("," identifier)* ")" | "(" ")"')
        #@self.pg.production('brace_block = "{" code  "}"')

        #-----------------------------------------------------------------------
        #@self.pg.production('if expression : expression')

        @self.pg.production('expression : LET VAR ASSIGN expression')
        @self.pg.production('expression : VAR ASSIGN expression')
        def assignment(p):
            if p[0].value == 'let':
                return Assign(p[1].value, p[3].eval(), self.binding)
            else:
                return Assign(p[0].value, p[2].eval(), self.binding)

        @self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def output(p):
            return Print(p[2], self.binding)

        @self.pg.production('expression : VAR')
        def variable(p):
            return Variable(p[0].value, self.binding)

        #fix this
        @self.pg.production('expression : expression COMMA expression')
        def comma(p):
            #p[0].eval()
            return p[0], p[2]


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

    def get_parser(self):
        return self.pg.build()
