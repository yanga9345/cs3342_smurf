class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

# Not sure about how im supposed to do this
#class Assign():
#    def __init__(self, value):


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


#class Assignment():
#    def __init__(self, left, right, variables):
#        self.left = left
#        self.right = right
#        self.variables = variables

# working on this
class Assign():
    def __init__(self, left, right, variables):
        self.left = left
        self.right = right
        self.variables = variables

    def eval(self):
        self.variables[self.left] = self.right

class Print:
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())
