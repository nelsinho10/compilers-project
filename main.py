from Core.lexicalAnalyzer.LexicalAnalyzer import LexicalAnalyzer
from Core.syntacticAnalyzer.syntacticAnalyzer import Syntactic
from Core.Reader import Reader
from tabulate import tabulate

reader = Reader().read()
name = Reader().read().fileName

if reader.instruction == None:
    print("\n----------------Ejecutando Traduccion------------------\n")
    text = LexicalAnalyzer(reader,name).processText().identifyToken().text
    Syntactic(text).run()

elif reader.instruction == "--analisis-lexico":
    print("\n--------------Ejecutando Analisis Lexico--------------\n")
    tokens = LexicalAnalyzer(reader,name).processText().identifyToken().patterns
    headers = ['# Linea','Token','Descripcion']
    if len(tokens) > 0:
        print(tabulate(tokens, headers, tablefmt="grid"))
    else:
        print("No se encontraron ocurrencias")

elif reader.instruction == "--arbol-sintactico":
    print("--------------Ejecutando Arbol Sintactico--------------")
    text = LexicalAnalyzer(reader,name).processText().identifyToken().text
    Syntactic(text).tree()
else:
    quit("No se especifica instrucción o programa a analizar.")
