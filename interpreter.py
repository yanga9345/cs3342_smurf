# Interprets the AST


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


class BuiltInFunction:
    # built-in functions are print, and ()
    def __init__(self, func_name, call_args):
        self.func_name = func_name
        self.call_args = call_args

    def eval(self, binding):
        args = self.call_args.eval(binding)
        if self.func_name == "print":
            if type(args) == int:
                print(args)
            else:
                print("Print: ")
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
            return args[0]


# binding class used to store variables and functions
class Binding:
    def __init__(self, parent, binding):
        self.parent = parent
        self.binding = binding

    def get(self, name):
        if name in self.binding:
            return self.binding[name]
        return self.parent.get(name)

    def add(self, var_name, value):
        self.binding[var_name] = value

    def contains(self, name):
        for i in self.binding:
            if i == name:
                return True
        if self.parent:
            return self.parent.contains(name)
        return False


class FunctionCall:
    def __init__(self, func_name, call_args):
        self.func_name = func_name
        self.call_args = call_args

    def eval(self, binding):
        # if function has no parameters
        if type(self.call_args) == VarReference:
            args = self.call_args.eval(binding)
            return args[1].eval(binding)

        # else
        # creates a new function binding that is a child of the binding when the function was created
        func_binding = Binding(binding.get(self.func_name.value)[2], {})
        # sets parameters and arguments and adds them to the function binding
        parameters = self.call_args[0].eval(func_binding)[0]
        # checks to see if the arg values for param_list are in the function binding. This is for recursion.
        if func_binding.contains(parameters[0]):
            args = self.call_args[1].eval(func_binding)
        # if not, checks if the arg values are in the global binding
        else:
            args = self.call_args[1].eval(binding)

        # assigns the arg values to the parameters and adds it to the function binding
        for i in range(len(parameters)):
            func_binding.add(parameters[i], args[i])

        # returns the evaluated code using the function binding
        code = func_binding.get(self.func_name.value)[1]
        return code.eval(func_binding)


class FunctionDefinition:
    def __init__(self, param_list, code_block):
        self.param_list = param_list
        self.code_block = code_block

    def eval(self, binding):
        # creates a new binding
        func_binding = Binding(binding, {})
        # used to store a function's parameters, code, and function binding in global binding
        return self.param_list, self.code_block, func_binding


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
        binding.add(self.var_name, var_val)
        return var_val


class Assignment:
    def __init__(self, var_name, val):
        self.var_name = var_name
        self.val = val

    def eval(self, binding):
        var_val = self.val.eval(binding)
        binding.add(self.var_name, var_val)
        return var_val


class VarReference:
    def __init__(self, var_name):
        self.var_name = var_name

    def eval(self, binding):
        return binding.get(self.var_name)


class EqualTo(BinaryOp):
    def eval(self, binding):
        if self.left.eval(binding) == self.right.eval(binding):
            return 1
        else:
            return 0


class NotEqualTo(BinaryOp):
    def eval(self, binding):
        if self.left.eval(binding) != self.right.eval(binding):
            return 1
        else:
            return 0


class LessThan(BinaryOp):
    def eval(self, binding):
        if self.left.eval(binding) < self.right.eval(binding):
            return 1
        else:
            return 0


class LessThanOrEqualTo(BinaryOp):
    def eval(self, binding):
        if self.left.eval(binding) <= self.right.eval(binding):
            return 1
        else:
            return 0


class GreaterThan(BinaryOp):
    def eval(self, binding):
        if self.left.eval(binding) > self.right.eval(binding):
            return 1
        else:
            return 0


class GreaterThanOrEqualTo(BinaryOp):
    def eval(self, binding):
        if self.left.eval(binding) >= self.right.eval(binding):
            return 1
        else:
            return 0


class IfExpression:
    def __init__(self, bool_expr, if_block):
        self.bool_expr = bool_expr
        self.if_block = if_block

    def eval(self, binding):
        bool_result = self.bool_expr.eval(binding)
        if type(bool_result) is not int:
            bool_result = bool_result[0]
        if bool_result == 1:
            return self.if_block.eval(binding)
        else:
            return 0


class IfElseExpression:
    def __init__(self, bool_expr, if_block, else_block):
        self.bool_expr = bool_expr
        self.if_block = if_block
        self.else_block = else_block

    def eval(self, binding):
        bool_result = self.bool_expr.eval(binding)
        if type(bool_result) is not int:
            bool_result = bool_result[0]
        if bool_result == 1:
            return self.if_block.eval(binding)
        else:
            return self.else_block.eval(binding)

