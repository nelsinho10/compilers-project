from lark import Transformer, v_args
import re


@v_args(inline=True)
class Semantic(Transformer):
    def __init__(self):
        self.variables = {}

    def add(self, A, B):
        return float(A) + float(B)

    def sub(self, A, B):
        return float(A) - float(B)

    def mul(self, A, B):
        return float(A) * float(B)

    def div(self, A, B):
        return float(A) / float(B)

    def assignvar(self, name, value):
        self.variables[name] = value

    def getvar(self, name):
        return self.variables[name]

    def print(self, param):
        print("%s" % self.cleanParam(param))

    def printvar(self, name):
        print("%s" % (self.getvar(name)))

    def repeat(self, number, param):
        r = int(number) * self.cleanParam(param)
        return r

    def concat(self, var1, var2):
        varClean1 = self.variables[var1]
        varClean2 = self.variables[var2]
        return "%s %s" % (self.cleanParam(varClean1), self.cleanParam(varClean2))

    def cleanParam(self, param):
        if re.match(r"^\'[^\']*\'$", param):
            return param[1:-1]
        else:
            return param
