from flask import Blueprint, request, jsonify
from models import Sorteo
from connection import SessionLocal

sorteo_bp = Blueprint('sorteo_bp', __name__)

@sorteo_bp.route('/obtener', methods=['GET'])
def get_sorteos():
    try:
        with SessionLocal() as session:
            sorteos = session.query(Sorteo).all()
            if sorteos:
                return jsonify([s.to_dict() for s in sorteos]), 200
            return jsonify({'message': 'No se encontraron sorteos'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

@sorteo_bp.route('/crear', methods=['POST'])
def create_sorteo():
    try:
        data = request.get_json()
        required = ('id_rifa', 'numero_ganador')
        if not all(k in data for k in required):
            return jsonify({'message': 'Faltan datos requeridos'}), 400

        sorteo = Sorteo(
            id_rifa=data['id_rifa'],
            numero_ganador=data['numero_ganador']
        )
        with SessionLocal() as session:
            session.add(sorteo)
            session.commit()
            return jsonify({
                'message': 'Sorteo creado exitosamente',
                'sorteo': sorteo.to_dict()
            }), 201
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id_rifa": 3,
      "numero_ganador": 1234
    }
    '''

@sorteo_bp.route('/actualizar', methods=['PUT'])
def update_sorteo():
    try:
        data = request.get_json()
        if 'id' not in data:
            return jsonify({'message': 'Se requiere el campo id'}), 400

        with SessionLocal() as session:
            sorteo = session.query(Sorteo).filter_by(id=data['id']).first()
            if not sorteo:
                return jsonify({'message': 'Sorteo no encontrado'}), 404

            sorteo.id_rifa = data['id_rifa']
            sorteo.numero_ganador = data['numero_ganador']
            session.commit()

            return jsonify({
                'message': 'Sorteo actualizado exitosamente',
                'sorteo': sorteo.to_dict()
            }), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id": 1,
      "id_rifa": 3,
      "numero_ganador": 4321
    }
    '''

@sorteo_bp.route('/eliminar', methods=['DELETE'])
def delete_sorteo():
    try:
        data = request.get_json()
        if 'id' not in data:
            return jsonify({'message': 'Se requiere el campo id'}), 400

        with SessionLocal() as session:
            sorteo = session.query(Sorteo).filter_by(id=data['id']).first()
            if not sorteo:
                return jsonify({'message': 'Sorteo no encontrado'}), 404

            session.delete(sorteo)
            session.commit()
            return jsonify({'message': 'Sorteo eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id": 1
    }
    '''