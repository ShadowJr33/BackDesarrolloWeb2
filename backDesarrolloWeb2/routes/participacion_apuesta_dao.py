from flask import Blueprint, request, jsonify
from models import ParticipacionApuesta
from connection import SessionLocal

participacion_apuesta_bp = Blueprint('participacion_apuesta_bp', __name__)

@participacion_apuesta_bp.route('/obtener', methods=['GET'])
def get_participaciones_apuesta():
    try:
        with SessionLocal() as session:
            partidas = session.query(ParticipacionApuesta).all()
            if partidas:
                return jsonify([p.to_dict() for p in partidas]), 200
            return jsonify({'message': 'No se encontraron participaciones de apuesta'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

@participacion_apuesta_bp.route('/crear', methods=['POST'])
def create_participacion_apuesta():
    try:
        data = request.get_json()
        required = ('id_apuesta', 'id_usuario', 'valor_apostado')
        if not all(k in data for k in required):
            return jsonify({'message': 'Faltan datos requeridos'}), 400

        participacion = ParticipacionApuesta(
            id_apuesta=data['id_apuesta'],
            id_usuario=data['id_usuario'],
            valor_apostado=data['valor_apostado']
        )
        with SessionLocal() as session:
            session.add(participacion)
            session.commit()
            return jsonify({
                'message': 'Participación de apuesta creada exitosamente',
                'participacion': participacion.to_dict()
            }), 201
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id_apuesta": 3,
      "id_usuario": 5,
      "valor_apostado": 250.0
    }
    '''

@participacion_apuesta_bp.route('/actualizar', methods=['PUT'])
def update_participacion_apuesta():
    try:
        data = request.get_json()
        if 'id' not in data:
            return jsonify({'message': 'Se requiere el campo id'}), 400

        with SessionLocal() as session:
            participacion = session.query(ParticipacionApuesta).filter_by(id=data['id']).first()
            if not participacion:
                return jsonify({'message': 'Participación no encontrada'}), 404

            participacion.id_apuesta   = data['id_apuesta']
            participacion.id_usuario   = data['id_usuario']
            participacion.valor_apostado = data['valor_apostado']
            session.commit()

            return jsonify({
                'message': 'Participación de apuesta actualizada exitosamente',
                'participacion': participacion.to_dict()
            }), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id": 1,
      "id_apuesta": 4,
      "id_usuario": 5,
      "valor_apostado": 300.0
    }
    '''
@participacion_apuesta_bp.route('/eliminar', methods=['DELETE'])
def delete_participacion_apuesta():
    try:
        data = request.get_json()
        if 'id' not in data:
            return jsonify({'message': 'Se requiere el campo id'}), 400

        with SessionLocal() as session:
            participacion = session.query(ParticipacionApuesta).filter_by(id=data['id']).first()
            if not participacion:
                return jsonify({'message': 'Participación no encontrada'}), 404

            session.delete(participacion)
            session.commit()
            return jsonify({'message': 'Participación de apuesta eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id": 1
    }
    '''