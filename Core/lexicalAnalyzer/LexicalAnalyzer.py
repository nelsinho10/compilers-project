import re

class LexicalAnalyzer:
    def __init__(self,reader):
        self.reader = reader
        self.text = self.reader.text
        self.patterns = []

    def processText(self):
        text = re.sub(r'\s+', ' ', self.text)
        self.tokens = re.split(r'\s', text)
        return self
        
    def identifyToken(self):
        patterns = []

        for token in self.tokens:
            token = ('%s'.strip() % token).strip() #Limpiar el token
            
            if len(token) > 0:

                #idenfificador de variable
                if re.match(r'^siuu$',token):
                    patterns.append([token,'Identificador de variable'])
                
                #Identificar de usuario
                elif re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$',token):
                    patterns.append([token,'Identificador de usuario'])
                
                #Operador de asignacion
                elif re.match(r'^=$',token):
                    patterns.append([token,'Operador de asignacion'])

                #Operador de fin de Instruccion
                elif re.match(r'^\$$',token):
                    patterns.append([token,'Identificador de fin de instruccion'])

                #Numero flotante
                elif re.match(r'^\d+\.\d+$',token):
                    patterns.append([token,'Numero flotante'])

                #Identificar palabras con 3 vocales
                elif re.match(r'^\d+$',token):
                    patterns.append([token,'tres o mas vocales iguales en una palabra'])
                else:
                    pass
        
        self.patterns = patterns

        return self

        