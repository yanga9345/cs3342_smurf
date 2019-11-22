class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class Boolean():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mult(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return int(self.left.eval() / self.right.eval())


class Assign():
    def __init__(self, left, right, binding):
        self.left = left
        self.right = right
        self.binding = binding

    def eval(self):
        self.binding[self.left] = self.right


class Variable():
    def __init__(self, name, binding):
        self.name = name
        self.binding = binding

    def eval(self):
        return int(self.binding[self.name])


class Print:
    def __init__(self, value, binding):
        self.value = value
        self.binding = binding

    def print_all(self, val):
        if isinstance(val, tuple):
            for element in val:
                self.print_all(element)
        else:
            print(val.eval())

    def eval(self):
        self.print_all(self.value)
        #print(self.value.eval())
        #evaluate_children(print, self.value)


# def evaluate_children(function, value):
#    if isinstance(value, tuple):
#        for element in value:
#            evaluate_children(function, element)
#    else:
#        function(value.eval())
