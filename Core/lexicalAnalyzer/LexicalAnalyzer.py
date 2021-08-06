import re


class LexicalAnalyzer:
    def __init__(self, reader, name):
        self.reader = reader
        self.fileName = name
        self.text = self.reader.text
        self.patterns = []
        self.acum = []

    def processText(self):
        text = re.sub(r"\s+", " ", self.text)
        self.tokens = re.split(r"\s", text)
        return self

    def identifyToken(self):
        patterns = []

        for token in self.tokens:
            token = ("%s".strip() % token).strip()  # Limpiar el token

            if len(token) > 0:
                if re.match(r"\'[^\']*\'", token):
                    patterns.append([self.searchTokenLine(token),token, "Identificador de cadena"])

                # Identificar de usuario
                elif re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", token):
                    patterns.append([self.searchTokenLine(token), token, "Identificador de usuario"])

                # Operador de asignacion
                elif re.match(r"^=$", token):
                    patterns.append([self.searchTokenLine(token), token, "Operador de asignacion"])

                # Operador de fin de Instruccion
                elif re.match(r"^\$$", token):
                    patterns.append([self.searchTokenLine(token), token, "Identificador de fin de instruccion"])

                # Numero
                elif re.match(r"^\d+(\.\d+)?$", token):
                    patterns.append([self.searchTokenLine(token), token, "Numero"])

                # Operador Aritmetico
                elif re.match(r"^[\+|\-\*\/]$", token):
                    patterns.append([self.searchTokenLine(token), token, "Operador Aritmetico"])

                # Operador de repeticion
                elif re.match(r"^\#$", token):
                    patterns.append([self.searchTokenLine(token), token, "Operador de repeticion"])
                
                # Operador de concatenacion
                elif re.match(r"^\:$", token):
                    patterns.append([self.searchTokenLine(token), token, "Operador de concatenacion"])

                else:
                    quit(
                        "Error: \n\tSe ha encontrado un token desconocido en la linea %s: %s \n\n" % (
                            self.searchTokenLineError(token),
                            token
                        )
                    )

        self.patterns = patterns

        return self

    def searchTokenLineError(self, token):
        errorLine = 0

        f = open(self.fileName, 'r')
        for line in f:
            errorLine += 1
            if re.match(r'^.*%s.*$' % self.prevent(token), line):

                break
        return errorLine

    def searchTokenLine(self, token):
        l = 0
        return l    

    def prevent(self, token):

        if re.match(r'[\+\*\.\(\)\{\}\[\]\\\<\>]', token):
            return '\\%s' % token


