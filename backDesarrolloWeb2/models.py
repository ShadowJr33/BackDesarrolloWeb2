from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Date
from conection import Base


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


class Apuesta(Base):
    __tablename__ = "apuesta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    deporte = Column(String(50), nullable=False)
    campeonato = Column(String(100), nullable=False)
    fecha_partido = Column(DateTime, nullable=False, name="fechaPartido")
    marcador = Column(String(20), nullable=True)
    valor_minimo_apuesta = Column(Float, nullable=False, name="valorMinimoApuesta")
    valor_maximo_apuesta = Column(Float, nullable=False, name="valorMaximoApuesta")


    def __str__(self):
        return (f'ID: {self.id}, Deporte: {self.deporte}, Campeonato: {self.campeonato}, '
                f'Fecha Partido: {self.fecha_partido}, Marcador: {self.marcador}, '
                f'Valor Mínimo Apuesta: {self.valor_minimo_apuesta}, Valor Máximo Apuesta: {self.valor_maximo_apuesta}')

    
class Boleto(Base):
    __tablename__ = "boleto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_rifa = Column(ForeignKey("rifa.Id"), nullable=False, name="idRifa")
    id_usuario = Column(ForeignKey("usuario.id"), nullable=False, name="idUsuario")
    numero_asignado = Column(Integer, nullable=False, name="numeroAsignado")

    def __str__(self):
        return (f'ID: {self.id}, ID Rifa: {self.id_rifa}, '
                f'ID Usuario: {self.id_usuario}, Número Asignado: {self.numero_asignado}')


class ParticipacionApuesta(Base):
    __tablename__ = "participacionApuesta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_apuesta = Column(ForeignKey("apuesta.id"), nullable=False, name="idApuesta")
    id_usuario = Column(ForeignKey("usuario.id"), nullable=False, name="idUsuario")
    valor_apostado = Column(Float, nullable=False, name="valorApostado")

    def __str__(self):
        return (f'ID: {self.id}, ID Apuesta: {self.id_apuesta}, '
                f'ID Usuario: {self.id_usuario}, Valor Apostado: {self.valor_apostado}')


class Sorteo(Base):
    __tablename__ = "sorteo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_rifa = Column("idRifa", ForeignKey("rifa.Id"), nullable=False)
    numero_ganador = Column("numeroGanador", Integer, nullable=False)

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
