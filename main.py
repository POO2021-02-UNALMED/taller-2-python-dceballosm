class Asiento:
    def _init_(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        if isinstance(color, 'str'):
            if color in ['rojo','verde','amarillo','negro','blanco']:
                self.color = color

class Auto:
    cantidadCreados = 0
    
    def _init_(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.registro = registro
        
    def cantidadAsientos(self):
        contador_asientos = 0
        for asiento_ in self.asientos:
            if isinstance(asiento_, Asiento):
                contador_asientos += 1
        return contador_asientos
        
    def verificarIntegridad(self):
        if (self.motor.registro == self.registro):
            for asiento_ in self.asientos:
                if asiento_.registro != self.registro:
                    return 'Las piezas no son originales'
            return 'Auto original'    
        else:
            return 'Las piezas no son originales'
        
        
class Motor:
    
    def _init_(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro):
        if isinstance(registro, int):
            self.registro = registro
        
    def asignarTipo(self, tipo):
        if isinstance(tipo, str):
            if tipo in ['electrico','gasolina']:
                self.tipo = tipo
        
