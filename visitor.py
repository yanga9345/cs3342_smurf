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

    #def visit_statement(self, node, children):
    #    return children[0]

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


    #def visit_call_arguments(self, node, children):
    #    args = []
    #    for arg in children:
    #        args.append(arg)
    #    return args