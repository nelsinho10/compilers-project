from Core.lexicalAnalyzer.LexicalAnalyzer import LexicalAnalyzer
from Core.syntacticAnalyzer.syntacticAnalyzer import Syntactic
from Core.Reader import Reader
from tabulate import tabulate

reader = Reader().read()

if reader.instruction == None:
    print("----------------Ejecutando Traduccion------------------\n\n")
    text = LexicalAnalyzer(reader).processText().identifyToken().text
    Syntactic(text).run()

elif reader.instruction == "--analisis-lexico":
    print("--------------Ejecutando Analisis Lexico--------------\n\n")
    tokens = LexicalAnalyzer(reader).processText().identifyToken().patterns
    print("Tokens encontrados:")
    if len(tokens) > 0:
        print(tabulate(tokens))
    else:
        print("No se encontraron ocurrencias")

elif reader.instruction == "--arbol-sintactico":
    print("--------------Ejecutando Arbol Sintactico--------------")
    text = LexicalAnalyzer(reader).processText().identifyToken().text
    Syntactic(text).tree()
else:
    quit("No se especifica instrucción o programa a analizar.")
