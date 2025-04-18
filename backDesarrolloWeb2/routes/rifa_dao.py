from flask import Blueprint, request, jsonify
from models import Rifa
from connection import SessionLocal  # Ajusta si tu estructura cambia

rifa_bp = Blueprint('rifa_bp', __name__)

@rifa_bp.route('/obtener', methods=['GET'])
def get_rifas():
    try:
        with SessionLocal() as session:
            rifas = session.query(Rifa).all()
            if rifas:
                return jsonify([r.to_dict() for r in rifas]), 200
            return jsonify({'message': 'No se encontraron rifas'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

@rifa_bp.route('/crear', methods=['POST'])
def create_rifa():
    
    try:
        data = request.get_json()
        required = ('nombre','numero_maximo_participantes','valor','fecha_inicio','fecha_fin','premio_principal')
        if not all(k in data for k in required):
            return jsonify({'message': 'Faltan datos requeridos'}), 400

        rifa = Rifa(
            nombre=data['nombre'],
            numero_maximo_participantes=data['numero_maximo_participantes'],
            valor=data['valor'],
            fecha_inicio=data['fecha_inicio'],
            fecha_fin=data['fecha_fin'],
            premio_principal=data['premio_principal'],
            premios_secundarios=data.get('premios_secundarios')
        )
        with SessionLocal() as session:
            session.add(rifa)
            session.commit()
            return jsonify({'message': 'Rifa creada exitosamente', 'rifa': rifa.to_dict()}), 201
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "nombre": "Gran Rifa 2025",
      "numero_maximo_participantes": 1000,
      "valor": 50.0,
      "fecha_inicio": "2025-05-01",
      "fecha_fin": "2025-05-31",
      "premio_principal": "Auto último modelo",
      "premios_secundarios": "TV, Laptop"
    }
    '''

@rifa_bp.route('/actualizar', methods=['PUT'])
def update_rifa():
    
    try:
        data = request.get_json()
        required = {
            'id', 'nombre', 'numero_maximo_participantes', 'valor',
            'fecha_inicio', 'fecha_fin', 'premio_principal'
        }
        if not required.issubset(data):
            return jsonify({'message': f'Faltan campos requeridos: {required - data.keys()}'}), 400

        from datetime import datetime
        with SessionLocal() as session:
            rifa = session.query(Rifa).filter_by(id=data['id']).first()
            if not rifa:
                return jsonify({'message': 'Rifa no encontrada'}), 404

            rifa.nombre = data['nombre']
            rifa.numero_maximo_participantes = data['numero_maximo_participantes']
            rifa.valor = data['valor']
            rifa.fecha_inicio = datetime.strptime(data['fecha_inicio'], '%Y-%m-%d').date()
            rifa.fecha_fin    = datetime.strptime(data['fecha_fin'], '%Y-%m-%d').date()
            rifa.premio_principal   = data['premio_principal']
            rifa.premios_secundarios = data.get('premios_secundarios')  # opcional

            session.commit()
            return jsonify({'message': 'Rifa actualizada completamente', 'rifa': rifa.to_dict()}), 200

    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id": 1,
      "nombre": "Rifa Todo Actualizado",
      "numero_maximo_participantes": 500,
      "valor": 75.0,
      "fecha_inicio": "2025-06-01",
      "fecha_fin": "2025-06-30",
      "premio_principal": "Bicicleta eléctrica",
      "premios_secundarios": "Smartwatch, Tablet"
    }
    '''

@rifa_bp.route('/eliminar', methods=['DELETE'])
def delete_rifa():
    try:
        data = request.get_json()
        if 'id' not in data:
            return jsonify({'message': 'Se requiere el campo id'}), 400

        with SessionLocal() as session:
            rifa = session.query(Rifa).filter_by(id=data['id']).first()
            if not rifa:
                return jsonify({'message': 'Rifa no encontrada'}), 404

            session.delete(rifa)
            session.commit()
            return jsonify({'message': 'Rifa eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
      "id": 1
    }
    '''