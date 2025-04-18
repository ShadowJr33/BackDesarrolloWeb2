from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Date
from datetime import datetime
from connection import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    contraseña = Column(String(100), nullable=False)
    saldo = Column(Float, default=0.0)

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Correo: {self.correo}, Saldo: {self.saldo}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo,
            'saldo': self.saldo
        }

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
        
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'numero_maximo_participantes': self.numero_maximo_participantes,
            'valor': self.valor,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin,
            'premio_principal': self.premio_principal,
            'premios_secundarios': self.premios_secundarios
        }

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
        
    def to_dict(self):
        return {
            'id': self.id,
            'deporte': self.deporte,
            'campeonato': self.campeonato,
            'fecha_partido': self.fecha_partido,
            'marcador': self.marcador,
            'valor_minimo_apuesta': self.valor_minimo_apuesta,
            'valor_maximo_apuesta': self.valor_maximo_apuesta
        }

    
class Boleto(Base):
    __tablename__ = "boleto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_rifa = Column(ForeignKey("rifa.Id"), nullable=False, name="idRifa")
    id_usuario = Column(ForeignKey("usuario.id"), nullable=False, name="idUsuario")
    numero_asignado = Column(Integer, nullable=False, name="numeroAsignado")

    def __str__(self):
        return (f'ID: {self.id}, ID Rifa: {self.id_rifa}, '
                f'ID Usuario: {self.id_usuario}, Número Asignado: {self.numero_asignado}')
   
    def to_dict(self):
        return {
            'id': self.id,
            'id_rifa': self.id_rifa,
            'id_usuario': self.id_usuario,
            'numero_asignado': self.numero_asignado
        }

class ParticipacionApuesta(Base):
    __tablename__ = "participacionApuesta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_apuesta = Column(ForeignKey("apuesta.id"), nullable=False, name="idApuesta")
    id_usuario = Column(ForeignKey("usuario.id"), nullable=False, name="idUsuario")
    valor_apostado = Column(Float, nullable=False, name="valorApostado")

    def __str__(self):
        return (f'ID: {self.id}, ID Apuesta: {self.id_apuesta}, '
                f'ID Usuario: {self.id_usuario}, Valor Apostado: {self.valor_apostado}')
        
    def to_dict(self):
        return {
            'id': self.id,
            'id_apuesta': self.id_apuesta,
            'id_usuario': self.id_usuario,
            'valor_apostado': self.valor_apostado
        }


class Sorteo(Base):
    __tablename__ = "sorteo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_rifa = Column("idRifa", ForeignKey("rifa.Id"), nullable=False)
    numero_ganador = Column("numeroGanador", Integer, nullable=False)

    def __str__(self):
        return (f'ID: {self.id}, ID Rifa: {self.id_rifa}, Número Ganador: {self.numero_ganador}')
    
    def to_dict(self):
        return {
            'id': self.id,
            'id_rifa': self.id_rifa,
            'numero_ganador': self.numero_ganador
        }


class PagoPremio(Base):
    __tablename__ = "pagoPremio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column("idUsuario", ForeignKey("usuario.id"), nullable=False)
    id_rifa_apuesta = Column("idRifa_Apuesta", Integer, nullable=False)
    valor_ganado = Column("valorGanado", Float, nullable=False)

    def __str__(self):
        return (f'ID: {self.id}, Usuario ID: {self.id_usuario}, '
                f'Rifa/Apuesta ID: {self.id_rifa_apuesta}, Valor Ganado: {self.valor_ganado}')
    def to_dict(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_rifa_apuesta": self.id_rifa_apuesta,
            "valor_ganado": self.valor_ganado            
        }


class Transaccion(Base):
    __tablename__ = "transaccion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column("idUsuario", ForeignKey("usuario.id"), nullable=False)
    tipo = Column(String(20), nullable=False)  # ENUM no es soportado directamente por SQLite
    monto = Column(Float, nullable=False)
    fecha = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __str__(self):
        return (f'ID: {self.id}, Usuario ID: {self.id_usuario}, Tipo: {self.tipo}, '
                f'Monto: {self.monto}, Fecha: {self.fecha}')

    def to_dict(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "tipo": self.tipo,
            "monto": self.monto,
            "fecha": self.fecha
        }