from arpeggio import PTNodeVisitor

class Interpreter:
    def __init__(self):
        self.binding = {}

    def evaluate_integer(self, node, children):
        return int(node.value)

    def evaluate_primary(self, node, children):
        return children[0]

    def evaluate_mult_term(self, node, children):
        expr = children[0]
        for i in range(2, len(children), 2):
            if i and children[i - 1] == "*":
                expr *= children[i]
            else:
                expr /= children[i]
        return int(expr)

    def evaluate_arithmetic_expression(self, node, children):
        expr = children[0]
        for i in range(2, len(children), 2):
            if i and children[i - 1] == "-":
                expr -= children[i]
            else:
                expr += children[i]
        return expr

    def evaluate_function_call(self, node, children):
        if children[0] == "print":
            print(children[1])
            return children[1]
        return children[0]

    def evaluate_variable_decl(self, node, children):
        #self.binding[node[0]] = children[0]
        return children[0]