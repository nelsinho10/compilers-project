import sys

class Reader():
    def __init__(self): 
        self.instruction = None
        self.fileName = None
        self.text = None

    def read(self):
        # Lectura de parámetros
        self.params = sys.argv[1:]

        # ? Casos para determinar la acción a realizar según los parámetros
        # * Acción de Interpretación
        try:
            if len(self.params) == 1:
                self.fileName =  self.params[0]
                f = open(self.fileName,'r')
                self.text = f.read()
                f.close()

            elif len(self.params) == 2:
                self.instruction = self.params[1]
                self.fileName = self.params[0]
                f = open(self.fileName,'r')
                self.text = f.read()
                f.close()

            else:
                quit("Error cantidad de parametros invalidos")
        except FileNotFoundError as e:
            quit("Error %s"%e)
        return self 