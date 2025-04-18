from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Transaccion
from connection import SessionLocal

transaccion_bp = Blueprint('transaccion_bp', __name__)

@transaccion_bp.route('/obtener', methods=['GET'])
def listar_transacciones():
    try:
        with SessionLocal() as session:
            transacciones = session.query(Transaccion).all()
            return jsonify([t.to_dict() for t in transacciones]), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500


@transaccion_bp.route('/crear', methods=['POST'])
def create_transaccion():
    '''
    Ejemplo JSON para probar:
    {
      "id_usuario": 5,
      "tipo": "credito",
      "monto": 150.0
    }
    '''
    try:
        data = request.get_json()
        required = ('id_usuario', 'tipo', 'monto')
        if not all(k in data for k in required):
            return jsonify({'message': 'Faltan datos requeridos'}), 400

        fecha = datetime.fromisoformat(data['fecha']) if 'fecha' in data else datetime.utcnow()

        trans = Transaccion(
            id_usuario=data['id_usuario'],
            tipo=data['tipo'],
            monto=data['monto'],
            fecha=fecha
        )
        with SessionLocal() as session:
            session.add(trans)
            session.commit()
            return jsonify({'message': 'Transacción creada exitosamente', 'transaccion': trans.to_dict()}), 201
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500


@transaccion_bp.route('/actualizar/<int:id>', methods=['PUT'])
def update_transaccion(id):
    '''
    Ejemplo JSON para probar:
    {
      "id_usuario": 5,
      "tipo": "debito",
      "monto": 100.0,
      "fecha": "2025-04-18T15:00:00"
    }
    '''
    try:
        data = request.get_json()
        with SessionLocal() as session:
            trans = session.query(Transaccion).filter_by(id=id).first()
            if not trans:
                return jsonify({'message': 'Transacción no encontrada'}), 404

            # Solo actualizamos si viene en el JSON
            if 'id_usuario' in data:
                trans.id_usuario = data['id_usuario']
            if 'tipo' in data:
                trans.tipo = data['tipo']
            if 'monto' in data:
                trans.monto = data['monto']
            if 'fecha' in data:
                trans.fecha = datetime.fromisoformat(data['fecha'])

            session.commit()
            return jsonify({'message': 'Transacción actualizada', 'transaccion': trans.to_dict()}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500


@transaccion_bp.route('/eliminar/<int:id>', methods=['DELETE'])
def delete_transaccion(id):
    try:
        with SessionLocal() as session:
            trans = session.query(Transaccion).filter_by(id=id).first()
            if not trans:
                return jsonify({'message': 'Transacción no encontrada'}), 404
            session.delete(trans)
            session.commit()
            return jsonify({'message': 'Transacción eliminada'}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
