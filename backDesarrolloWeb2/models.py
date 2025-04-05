from sqlalchemy import Column, Integer, String, Float, Date
from backDesarrolloWeb2.conection import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    contraseña = Column(String(100), nullable=False)
    saldo = Column(Float, default=0.0)

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Correo: {self.correo}, Saldo: {self.saldo}'

class Rifa(Base):
    __tablename__ = "rifa"  # Usa el nombre exacto de la tabla (respeta la mayúscula)

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    nombre = Column("Nombre", String(100), nullable=False)
    numero_maximo_participantes = Column("NumeroMaximoParticipantes", Integer, nullable=False)
    valor = Column("Valor", Float, nullable=False)
    fecha_inicio = Column("FechaInicio", Date, nullable=False)
    fecha_fin = Column("FechaFin", Date, nullable=False)
    premio_principal = Column("PremioPrincipal", String(255), nullable=False)
    premios_secundarios = Column("PremiosSecundarios", String(255))

    def __str__(self):
        return (f'ID: {self.id}, Nombre: {self.nombre}, Participantes: {self.numero_maximo_participantes}, '
                f'Valor: {self.valor}, Inicio: {self.fecha_inicio}, Fin: {self.fecha_fin}, '
                f'Premio Principal: {self.premio_principal}, Premios Secundarios: {self.premios_secundarios}')


class Apuesta:
    def __init__ (self, id=None, deporte=None, campeonato=None, fecha_partido=None, 
                  marcador=None, valor_minimo_apuesta=None, valor_maximo_apuesta=None):
        self.id = id
        self.deporte = deporte
        self.campeonato = campeonato
        self.fecha_partido = fecha_partido
        self.marcador = marcador
        self.valor_minimo_apuesta = valor_minimo_apuesta
        self.valor_maximo_apuesta = valor_maximo_apuesta
    
    def __str__(self):
        return (f'ID: {self.id}, Deporte: {self.deporte}, Campeonato: {self.campeonato}, '
                f'Fecha Partido: {self.fecha_partido}, Marcador: {self.marcador}, '
                f'Valor Minimo Apuesta: {self.valor_minimo_apuesta}, Valor Maximo Apuesta: {self.valor_maximo_apuesta}')
    
class Boleto:
    def __init__(self, id=None, id_rifa=None, id_usuario=None, numero_asignado=None):
        self.id = id
        self.id_rifa = id_rifa
        self.id_usuario = id_usuario
        self.numero_asignado = numero_asignado

    def __str__(self):
        return (f'ID: {self.id}, ID Rifa: {self.id_rifa}, '
                f'ID Usuario: {self.id_usuario}, Número Asignado: {self.numero_asignado}')


class ParticipacionApuesta:
    def __init__(self, id=None, id_apuesta=None, id_usuario=None, valor_apostado=None):
        self.id = id
        self.id_apuesta = id_apuesta
        self.id_usuario = id_usuario
        self.valor_apostado = valor_apostado

    def __str__(self):
        return (f'ID: {self.id}, ID Apuesta: {self.id_apuesta}, '
                f'ID Usuario: {self.id_usuario}, Valor Apostado: {self.valor_apostado}')


class Sorteo:
    def __init__(self, id=None, id_rifa=None, numero_ganador=None):
        self.id = id
        self.id_rifa = id_rifa
        self.numero_ganador = numero_ganador

    def __str__(self):
        return (f'ID: {self.id}, ID Rifa: {self.id_rifa}, Número Ganador: {self.numero_ganador}')

class PagoPremio:
    def __init__(self, id=None, idusuario=None, idrifa_apuesta=None, valorganado=None):
        self.id = id
        self.idusuario = idusuario
        self.idrifa_apuesta = idrifa_apuesta
        self.valorganado = valorganado

    def __str__(self):
        return (f'ID: {self.id}, Usuario ID: {self.idusuario}, Rifa/Apuesta ID: {self.idrifa_apuesta}, '
                f'Valor Ganado: {self.valorganado}')
class Transaccion:
    def __init__(self, id=None, idusuario=None, tipo=None, monto=None, fecha=None):
        self.id = id
        self.idusuario = idusuario
        self.tipo = tipo
        self.monto = monto
        self.fecha = fecha

    def __str__(self):
        return (f'ID: {self.id}, Usuario ID: {self.idusuario}, Tipo: {self.tipo}, '
                f'Monto: {self.monto}, Fecha: {self.fecha}')
