from arpeggio import PTNodeVisitor

class Visitor(PTNodeVisitor):
    binding = {}
    def visit_integer(self, node, children):
        return int(node.value)

    def visit_primary(self, node, children):
        return children[0]

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
        if node.value[0:end-1] == "print":
            print(children[0])
            #return children[0]
        #if children[0] == "print":
            #print(children[1])
            #return children[1]
        return children[0]

    def visit_variable_decl(self, node, children):
        end = node.value.find("|")
        var_name = node.value[0:end-1]
        self.binding[var_name] = children[0]
        return children[0]

    def visit_variable_reference(self, node, children):
        var = self.binding[node.value]
        return self.binding[node.value]

    def visit_identifier(self, node, children):
        return node.value

    def visit_assignment(self, node, children):
        self.binding[children[0]] = children[1]
        return children[1]

    #def visit_expr(self, node, children):
    #    return children[0]
    #def visit_call_arguments(self, node, children):
    #    args = []
    #    for arg in children:
    #        args.append(arg)
    #    return args