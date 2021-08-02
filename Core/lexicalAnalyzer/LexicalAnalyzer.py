import re

class LexicalAnalyzer:
    def __init__(self,reader):
        self.reader = reader
        self.text = self.reader.text

    def processText(self):
        text = re.sub(r'\s+', ' ', self.text)
        self.tokens = re.split(r'\s', text)
        return self
        
    def identifyToken(self):
        patterns = []

        for token in self.tokens:
            token = ('%s'.strip() % token).strip() #Limpiar el token
            
            if len(token) > 0:

                #Identificar secuencia de numeros
                if re.match(r'^$',token):
                    patterns.append([token,'Secuencia de numeros'])
                
                #Identificar numeros seguidos de letras y numeros
                elif re.match(r'^$',token):
                    patterns.append([token,'Secuencia de numeros seguido de secuencia de letras'])

                #Identificar vocales iguales
                elif re.match(r'^$',token):
                    patterns.append([token,'tres o mas vocales iguales en una palabra'])

                #Identificar caracteres especiales
                elif re.match(r'^$',token):
                    patterns.append([token,'caracteres especiales'])

                #Identificar palabras con 3 vocales
                elif re.match(r'^$',token):
                    patterns.append([token,'tres o mas vocales iguales en una palabra'])
                else:
                    pass

        return patterns