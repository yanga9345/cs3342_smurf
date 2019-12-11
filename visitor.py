# Builds the AST

from arpeggio import PTNodeVisitor
from interpreter import *


class Visitor(PTNodeVisitor):

    def visit_program(self, node, children):
        return Program(children[0])

    def visit_code(self, node, children):
        return Code(children)

    def visit_statement(self, node, children):
        return Statement(children[0])

    def visit_expr(self, node, children):
        return Expr(children[0])

    def visit_integer(self, node, children):
        return Integer(int(node.value))

    def visit_arithmetic_expression(self, node, children):
        if len(children) == 1:
            return children[0]
        else:
            if children[1] == "+":
                return Sum(children[0], children[2])
            else:
                return Sub(children[0], children[2])

    def visit_mult_term(self, node, children):
        if len(children) == 1:
            return children[0]
        else:
            if children[1] == "*":
                return Mult(children[0], children[2])
            else:
                return Div(children[0], children[2])

    def visit_function_call(self, node, children):
        if node[0].value == "print" or node[0].value == "(":
            return BuiltInFunction(node[0], children[0])
        if len(children) == 1:
            return FunctionCall(node[0], children[0])
        return FunctionCall(node[0], children)

    def visit_call_arguments(self, node, children):
        return CallArguments(children)

    def visit_variable_decl(self, node, children):
        return VariableDecl(children)

    def visit_decl(self, node, children):
        return Decl(children[0], children[1])

    def visit_assignment(self, node, children):
        return Assignment(children[0], children[1])

    def visit_variable_reference(self, node, children):
        return VarReference(node.value)

    def visit_boolean_expression(self, node, children):
        if children[1] == "==":
            return EqualTo(children[0], children[2])
        elif children[1] == "!=":
            return NotEqualTo(children[0], children[2])
        elif children[1] == ">":
            return GreaterThan(children[0], children[2])
        elif children[1] == ">=":
            return GreaterThanOrEqualTo(children[0], children[2])
        elif children[1] == "<":
            return LessThan(children[0], children[2])
        elif children[1] == "<=":
            return LessThanOrEqualTo(children[0], children[2])

    def visit_if_expression(self, node, children):
        if len(children) == 2:
            return IfExpression(children[0], children[1])
        else:
            return IfElseExpression(children[0], children[1], children[2])

    def visit_brace_block(self, node, children):
        return children[0]

    def visit_param_list(self, node, children):
        return children

    def visit_function_definition(self, node, children):
        return FunctionDefinition(children[0], children[1])
