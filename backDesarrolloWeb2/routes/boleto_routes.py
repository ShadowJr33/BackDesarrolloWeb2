from flask import Blueprint, request, jsonify
from models import Boleto  # 
from connection import SessionLocal  

boleto_bp = Blueprint('boleto_bp', __name__)


@boleto_bp.route('/obtener', methods=['GET'])
def get_boletos():
    try:
        with SessionLocal() as session:
            boletos = session.query(Boleto).all()
            if boletos:
                return jsonify([boleto.to_dict() for boleto in boletos])  
            return jsonify({'message': 'No boletos encontrados'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    

@boleto_bp.route('/crear', methods=['POST'])
def create_boleto():
    try:
        data = request.get_json()  
        
       
        if not all(key in data for key in ('id_rifa', 'id_usuario', 'numero_asignado')):
            return jsonify({'message': 'Faltan datos requeridos'}), 400  # Bad Request

        boleto = Boleto(
            id_rifa=data['id_rifa'],
            id_usuario=data['id_usuario'],
            numero_asignado=data['numero_asignado']
        )
        
        with SessionLocal() as session:
            session.add(boleto)
            session.commit() 
            return jsonify({'message': 'Boleto creado exitosamente'}), 201 

    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500 
    '''
    {
    "id_rifa": 4,
    "id_usuario": 2,
    "numero_asignado": 1
    }

    '''
# Ruta para actualizar un boleto
@boleto_bp.route('/actualizar', methods=['PUT'])
def update_boleto():
    try:
        data = request.get_json()
        if not all(key in data for key in ('id', 'id_rifa', 'id_usuario', 'numero_asignado')):
            return jsonify({'message': 'Faltan datos requeridos'}), 400

        id = data.get('id')
        with SessionLocal() as session:
            boleto = session.query(Boleto).filter_by(id=id).first()
            if boleto:
                boleto.id_rifa = data['id_rifa']
                boleto.id_usuario = data['id_usuario']
                boleto.numero_asignado = data['numero_asignado']
                session.commit()
                return jsonify({'message': 'Boleto actualizado exitosamente'}), 200
            return jsonify({'message': 'Boleto no encontrado'}), 404

    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
    "id_rifa": 5,
    "id_usuario": 3,
    "numero_asignado": 2
    }
    '''

@boleto_bp.route('/eliminar', methods=['DELETE'])
def delete_boleto():
    try:
        data = request.get_json()
        print("Payload recibido para eliminar:", data)  # <-- Agrega esto
        id = data.get('id')
        if id is None:
            return jsonify({'message': 'Falta id'}), 400
        with SessionLocal() as session:
            boleto = session.query(Boleto).filter_by(id=id).first()
            if boleto:
                session.delete(boleto)
                session.commit()
                return jsonify({'message': 'Boleto eliminado exitosamente'}), 200
            return jsonify({'message': 'Boleto no encontrado'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
'''
{
    "numero_asignado": 2
}

'''