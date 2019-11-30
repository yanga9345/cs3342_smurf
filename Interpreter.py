class Program:
    def __init__(self, code):
        self.code = code

    def eval(self, binding):
        return self.code.eval(binding)


class Code:
    def __init__(self, statements):
        self.statements = statements

    def eval(self, binding):
        val = 0
        for statement in self.statements:
            val = statement.eval(binding)
        return val


class Statement:
    def __init__(self, statement):
        self.statement = statement

    def eval(self, binding):
        return self.statement.eval(binding)


class Expr:
    def __init__(self, expression):
        self.expression = expression

    def eval(self, binding):
        return self.expression.eval(binding)


class Integer:
    def __init__(self, value):
        self.value = value

    def eval(self, binding):
        return int(self.value)


class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self, binding):
        return self.left.eval(binding) + self.right.eval(binding)


class Sub(BinaryOp):
    def eval(self, binding):
        return self.left.eval(binding) - self.right.eval(binding)


class Mult(BinaryOp):
    def eval(self, binding):
        return self.left.eval(binding) * self.right.eval(binding)


class Div(BinaryOp):
    def eval(self, binding):
        return int(self.left.eval(binding) / self.right.eval(binding))


class FunctionCall:
    def __init__(self, func_name, call_args):
        self.func_name = func_name
        self.call_args = call_args

    def eval(self, binding):
        args = self.call_args.eval(binding)
        out = ""
        if self.func_name == "print":
            if type(args) == int:
                print(args)
            else:
                count = 0
                for arg in args:
                    out = str(arg)
                    if count != len(args) - 1:
                        print(out, end="|")
                    else:
                        print(out)
                    count += 1
            return
        else:
            return args


class CallArguments:
    def __init__(self, arguments):
        self.arguments = arguments

    def eval(self, binding):
        arg_list = []
        for arg in self.arguments:
            arg_list.append(arg.eval(binding))
        return arg_list


class VariableDecl:
    def __init__(self, declarations):
        self.declarations = declarations

    def eval(self, binding):
        for decl in self.declarations:
            temp = decl.eval(binding)
        return temp


class Decl:
    def __init__(self, var_name, val):
        self.var_name = var_name
        self.val = val

    def eval(self, binding):
        var_val = self.val.eval(binding)
        binding[self.var_name] = var_val
        return var_val


class Assignment:
    def __init__(self, var_name, val):
        self.var_name = var_name
        self.val = val

    def eval(self, binding):
        var_val = self.val.eval(binding)
        binding[self.var_name] = var_val
        return var_val


class VarReference:
    def __init__(self, var_name):
        self.var_name = var_name

    def eval(self, binding):
        if self.var_name in binding:
            return binding[self.var_name]

