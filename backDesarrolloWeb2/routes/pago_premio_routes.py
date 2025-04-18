from flask import Blueprint, request, jsonify
from models import PagoPremio
from connection import SessionLocal

pago_premio_bp = Blueprint('pago_premio_bp', __name__)

@pago_premio_bp.route('/obtener', methods=['GET'])
def get_pagos():
    try:
        with SessionLocal() as session:
            pagos = session.query(PagoPremio).all()
            if pagos:
                return jsonify([p.to_dict() for p in pagos]), 200
            return jsonify({'message': 'No se encontraron pagos de premio'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

@pago_premio_bp.route('/crear', methods=['POST'])
def create_pago():
    try:
        data = request.get_json()
        required = ('id_usuario', 'id_rifa_apuesta', 'valor_ganado')
        if not all(k in data for k in required):
            return jsonify({'message': 'Faltan datos requeridos'}), 400

        pago = PagoPremio(
            id_usuario=data['id_usuario'],
            id_rifa_apuesta=data['id_rifa_apuesta'],
            valor_ganado=data['valor_ganado']
        )
        with SessionLocal() as session:
            session.add(pago)
            session.commit()
            return jsonify({'message': 'Pago de premio creado exitosamente',
                            'pago': pago.to_dict()}), 201
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id_usuario": 2,
      "id_rifa_apuesta": 5,
      "valor_ganado": 150.0
    }
    '''

@pago_premio_bp.route('/actualizar', methods=['PUT'])
def update_pago():
    try:
        data = request.get_json()
        if 'id' not in data:
            return jsonify({'message': 'Se requiere el campo id'}), 400

        with SessionLocal() as session:
            pago = session.query(PagoPremio).filter_by(id=data['id']).first()
            if not pago:
                return jsonify({'message': 'Pago de premio no encontrado'}), 404

            pago.id_usuario      = data['id_usuario']
            pago.id_rifa_apuesta = data['id_rifa_apuesta']
            pago.valor_ganado    = data['valor_ganado']
            session.commit()

            return jsonify({'message': 'Pago de premio actualizado exitosamente',
                            'pago': pago.to_dict()}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id": 3,
      "id_usuario": 2,
      "id_rifa_apuesta": 5,
      "valor_ganado": 200.0
    }
    '''

@pago_premio_bp.route('/eliminar', methods=['DELETE'])
def delete_pago():
    try:
        data = request.get_json()
        if 'id' not in data:
            return jsonify({'message': 'Se requiere el campo id'}), 400

        with SessionLocal() as session:
            pago = session.query(PagoPremio).filter_by(id=data['id']).first()
            if not pago:
                return jsonify({'message': 'Pago de premio no encontrado'}), 404

            session.delete(pago)
            session.commit()
            return jsonify({'message': 'Pago de premio eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id": 3
    }
    '''