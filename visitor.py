from arpeggio import PTNodeVisitor
from Interpreter import *


class Visitor(PTNodeVisitor):

    def visit_program(self, node, children):
        return Program(children[0])

    def visit_code(self, node, children):
        return Code(children)

    def visit_statement(self, node, children):
        return Statement(children[0])

    def visit_expr(self, node, children):
        if len(children) == 1:
            return Expr(children[0])
        else:
            return Expr(children[1])

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
        if node[0].value == "print" or "(":
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

def rambling():
   '''
    def visit_mult_term(self, node, children):
        expr = children[0]
        for i in range(2, len(children), 2):
            if i and children[i - 1] == "*":
                expr *= children[i]
            else:
                expr /= children[i]
        return int(expr)

    def visit_arithmetic_expression(self, node, children):
        expr = children[0]
        for i in range(2, len(children), 2):
            if i and children[i - 1] == "-":
                expr -= children[i]
            else:
                expr += children[i]
        return expr

    def visit_function_call(self, node, children):
        end = node.value.find("|")
        func_name = node.value[0:end - 1]

        if func_name == "print":
            if type(children[0]) is list:
                count = 0
                for i in children[0]:
                    if count != len(children[0]) - 1:
                        print(i, end="|")
                    else:
                        print(i)
                    count += 1
                return 0
            else:
                print(children[0])
                return children[0]
        return children[0]

    def visit_variable_decl(self, node, children):
        node_str = node.value
        for i in children:
            end = node_str.find("|")
            var_name = node_str[0:end - 1]
            self.binding[var_name] = i
            comma = node_str.find(",")
            node_str = node_str[comma+4:]

    def visit_decl(self, node, children):
        end = node.value.find("|")
        var_name = node.value[0:end - 1]
        self.binding[var_name] = children[1]
        return children[1]

    def visit_identifier(self, node, children):
        return node.value

    def visit_assignment(self, node, children):
        self.binding[children[0]] = children[1]
        return children[1]

    def visit_variable_reference(self, node, children):
        var_name = node.value
        if var_name in self.binding:
            return self.binding[var_name]

    def visit_call_arguments(self, node, children):
        if len(children) == 1:
            return children[0]
        call_args = []
        for arg in children:
            call_args.append(arg)
        return call_args

    def visit_if_expression(self, node, children):
        return children[0]

    def visit_brace_block(self, node, children):
        return children[0]

#    def visit_expr(self, node, children):
#        return children[0]
    '''