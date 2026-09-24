class Solicitud:
    def __init__(self, codigo: str, nombre: str, descripcion: str, hora_llegada: str):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.hora_llegada = hora_llegada

    def __str__(self):
        return f"{self.codigo} | {self.nombre} | {self.descripcion} | {self.hora_llegada}"