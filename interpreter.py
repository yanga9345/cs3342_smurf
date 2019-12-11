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


class Current:
    def __init__(self):
        """

        -----------------------------------------------------------------------------------------------------------------------------------------------------
        -----------------------------------------------------------------------------------------------------------------------------------------------------
        -----------------------------------------------------------------------------------------------------------------------------------------------------


        """


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

    def getBinding(self):
        return self.binding

    def addBinding(self, binding2):
        for i in binding2.getBinding:
            self.binding.add(i, binding2.get(i))

    def contains(self, name):
        for i in self.binding:
            if i == name:
                return True
        return False


class FunctionCall:
    def __init__(self, func_name, call_args):
        self.func_name = func_name
        self.call_args = call_args
        self.func_binding = {}

    def eval(self, binding):
        self.func_binding = binding.get(self.func_name.value)[2]
        if type(self.call_args) == VarReference:
            args = self.call_args.eval(self.func_binding)
            return args[1].eval(self.func_binding)
        else:
            parameters = self.call_args[0].eval(self.func_binding)[0]
            args = self.call_args[1].eval(self.func_binding)

            for i in range(len(parameters)):
                # binding[parameters[i]] = args[i]
                self.func_binding.add(parameters[i], args[i])
            #self.func_binding = binding[self.func_name.value][2]
            code = binding.get(self.func_name.value)[1]
            #self.func_binding = binding.get(self.func_name.value)[2]
            #for i in binding.getBinding:
                #if i not in self.func_binding and i != self.func_name.value :
                #if not self.func_binding.contains(i) and i != self.func_name.value :
                    #self.func_binding[i] = binding[i]
                    #self.func_binding.ad

            #parameters = self.call_args[0].eval(self.func_binding)[0]
            #args = self.call_args[1].eval(self.func_binding)

            #for i in range(len(parameters)):
                # binding[parameters[i]] = args[i]
            #    self.func_binding.add(parameters[i], args[i])
            #return binding[self.func_name.value][1].eval(binding)
            return code.eval(self.func_binding)


class FunctionDefinition:
    def __init__(self, param_list, code_block):
        self.param_list = param_list
        self.code_block = code_block
        self.func_binding = {}

    def eval(self, binding):
        self.func_binding = Binding(binding, {})
        return self.param_list, self.code_block, self.func_binding


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
        #binding[self.var_name] = var_val
        binding.add(self.var_name, var_val)
        return var_val


class Assignment:
    def __init__(self, var_name, val):
        self.var_name = var_name
        self.val = val

    def eval(self, binding):
        var_val = self.val.eval(binding)
        #binding[self.var_name] = var_val
        binding.add(self.var_name, var_val)
        return var_val


class VarReference:
    def __init__(self, var_name):
        self.var_name = var_name

    def eval(self, binding):
        #if self.var_name in binding:
            # return binding[self.var_name]
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
