from flask import Blueprint, request, jsonify
from models import Apuesta
from connection import SessionLocal
from datetime import datetime

apuesta_bp = Blueprint('apuesta_bp', __name__)

@apuesta_bp.route('/obtener', methods=['GET'])
def get_apuestas():
    try:
        with SessionLocal() as session:
            apuestas = session.query(Apuesta).all()
            if apuestas:
                return jsonify([a.to_dict() for a in apuestas]), 200
            return jsonify({'message': 'No se encontraron apuestas'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

@apuesta_bp.route('/crear', methods=['POST'])
def create_apuesta():
    try:
        data = request.get_json()
        required = ('deporte','campeonato','fecha_partido','valor_minimo_apuesta','valor_maximo_apuesta')
        if not all(k in data for k in required):
            return jsonify({'message': 'Faltan datos requeridos'}), 400

        fecha = datetime.fromisoformat(data['fecha_partido'])
        apuesta = Apuesta(
            deporte=data['deporte'],
            campeonato=data['campeonato'],
            fecha_partido=fecha,
            marcador=data.get('marcador'),
            valor_minimo_apuesta=data['valor_minimo_apuesta'],
            valor_maximo_apuesta=data['valor_maximo_apuesta']
        )
        with SessionLocal() as session:
            session.add(apuesta)
            session.commit()
            return jsonify({'message': 'Apuesta creada exitosamente', 'apuesta': apuesta.to_dict()}), 201
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "deporte": "Fútbol",
      "campeonato": "Liga MX",
      "fecha_partido": "2025-07-15T20:00:00",
      "marcador": "2-1",
      "valor_minimo_apuesta": 10.0,
      "valor_maximo_apuesta": 1000.0
    }
    '''

@apuesta_bp.route('/actualizar', methods=['PUT'])
def update_apuesta():
    try:
        data = request.get_json()
        required = {'id','deporte','campeonato','fecha_partido','valor_minimo_apuesta','valor_maximo_apuesta'}
        if not required.issubset(data):
            missing = required - data.keys()
            return jsonify({'message': f'Faltan campos requeridos: {missing}'}), 400

        with SessionLocal() as session:
            apuesta = session.query(Apuesta).filter_by(id=data['id']).first()
            if not apuesta:
                return jsonify({'message': 'Apuesta no encontrada'}), 404

            # Actualizamos todos los campos
            apuesta.deporte = data['deporte']
            apuesta.campeonato = data['campeonato']
            apuesta.fecha_partido = datetime.fromisoformat(data['fecha_partido'])
            apuesta.marcador = data.get('marcador')
            apuesta.valor_minimo_apuesta = data['valor_minimo_apuesta']
            apuesta.valor_maximo_apuesta = data['valor_maximo_apuesta']

            session.commit()
            return jsonify({'message': 'Apuesta actualizada exitosamente', 'apuesta': apuesta.to_dict()}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id": 1,
      "deporte": "Baloncesto",
      "campeonato": "NBA",
      "fecha_partido": "2025-08-01T19:30:00",
      "marcador": "102-99",
      "valor_minimo_apuesta": 20.0,
      "valor_maximo_apuesta": 2000.0
    }
    '''
    
@apuesta_bp.route('/eliminar', methods=['DELETE'])
def delete_apuesta():
    try:
        data = request.get_json()
        if 'id' not in data:
            return jsonify({'message': 'Se requiere el campo id'}), 400

        with SessionLocal() as session:
            apuesta = session.query(Apuesta).filter_by(id=data['id']).first()
            if not apuesta:
                return jsonify({'message': 'Apuesta no encontrada'}), 404

            session.delete(apuesta)
            session.commit()
            return jsonify({'message': 'Apuesta eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id": 1
    }
    '''
