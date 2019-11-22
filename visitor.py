from arpeggio import PTNodeVisitor


class Visitor(PTNodeVisitor):
    def visit_integer(self, node, children):
        return int(node.value)

    def visit_primary(self, node, children):
        return children[1]

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
        if children[0] == "print":
            print(children[1])
            return children[1]

    #def visit_call_arguments(self, node, children):
    #    args = []
    #    for arg in children:
    #        args.append(arg)
    #    return args