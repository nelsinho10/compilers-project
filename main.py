from Core.Reader import Reader
from Core.lexicalAnalyzer.LexicalAnalyzer import LexicalAnalyzer
from tabulate import tabulate
reader = Reader().read()

if reader.instruction == None:
    print('----------------Ejecutando Traduccion------------------')
   

elif reader.instruction == '--analisis-lexico':
    print('--------------Ejecutando Analisis Lexico--------------\n\n')
    tokens = LexicalAnalyzer(reader).processText().identifyToken()
    print('Tokens encontrados:')
    if len(tokens) > 0:
        print(tabulate(tokens))
    else:
        print('No se encontraron ocurrencias')

elif reader.instruction == '--arbol-sintactico':
    print('--------------Ejecutando Arbol Sintactico--------------')

else:
    quit('No se especifica instrucción o programa a analizar.')
