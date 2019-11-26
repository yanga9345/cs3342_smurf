from arpeggio import RegExMatch, Optional, ZeroOrMore, OneOrMore, EOF
# Smurf Syntax


def program():
    return (code, EOF)


def comment():
    return RegExMatch('#.*')


def code():
    return ZeroOrMore(statement)


def statement():
    return (ZeroOrMore('\n'), [("let", variable_decl), assignment, expr], ZeroOrMore('\n'))


def variable_decl():
    return (decl, ZeroOrMore((",", ZeroOrMore('\n'), decl)))


def decl():
    return (identifier, Optional(("=", expr)))


def identifier():
    return RegExMatch('\w*')


def variable_reference():
    return identifier


def if_expression():
    return (expr, brace_block, Optional(("else", brace_block)))


def assignment():
    return (identifier, "=", expr)


def expr():
    return [
            ("fn", function_definition),
            ("if", if_expression),
            boolean_expression,
            arithmetic_expression
    ]


def boolean_expression():
    return (arithmetic_expression, relop, arithmetic_expression)


def arithmetic_expression():
    return (mult_term, ZeroOrMore(addop, mult_term))


def mult_term():
    return (primary, ZeroOrMore(mulop, primary))


def primary():
    return [
        integer,
        function_call,
        variable_reference,
        ("(", arithmetic_expression, ")")
    ]


def integer():
    return RegExMatch('-?\d+')


def addop():
    return ["+", "-"]


def mulop():
    return ["*", "/"]


def relop():
    return [
        "==",
        "!=",
        ">=",
        ">",
        "<=",
        "<"
    ]


def function_call():
    return [
        ("print", "(", call_arguments, ")"),
        (variable_reference, "(", call_arguments, ")")]


def call_arguments():
    return Optional((expr, ZeroOrMore((",", expr))))


def function_definition():
    return (param_list, brace_block)


def param_list():
    return [
        ("(", identifier, ZeroOrMore((",", identifier)), ")"),
        ("(",")")
    ]


def brace_block():
    return ZeroOrMore('\n'), "{", ZeroOrMore('\n'), code, "}", ZeroOrMore('\n')