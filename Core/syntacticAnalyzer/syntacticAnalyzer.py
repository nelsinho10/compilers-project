from Core.syntacticAnalyzer.Grammar import *
from Core.syntacticAnalyzer.Semantic import Semantic
from lark import Lark, Transformer


class Syntactic:
    def __init__(self, text):
        self.text = text

    def run(self):
        parser = Lark(grammar, parser="lalr", transformer=Semantic())
        language = parser.parse
        sample = self.text

        try:
            language(sample)
        except Exception as e:
            print("Error: %s" % e)

    def tree(self):
        parser = Lark(grammar, parser="lalr")
        language = parser.parse
        sample = self.text

        try:
            print(language(sample).pretty())
        except Exception as e:
            print("Error: %s" % e)