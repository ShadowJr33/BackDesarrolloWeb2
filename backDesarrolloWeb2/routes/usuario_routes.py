from flask import Blueprint, request, jsonify
from models import Usuario
from connection import SessionLocal 

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/obtener', methods=['GET'])
def get_usuarios():
    try:
        with SessionLocal() as session:
            usuarios = session.query(Usuario).all() 
            if usuarios:
                return jsonify([usuario.to_dict() for usuario in usuarios]), 200
            return jsonify({'message': 'No usuarios encontrados'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500


@usuario_bp.route('/crear', methods=['POST'])
def create_usuario():
    try:
        data = request.get_json()  
        with SessionLocal() as session:
            usuario = Usuario(
                nombre=data['nombre'],
                correo=data['correo'],
                contraseña=data['contraseña'],
                saldo=data.get('saldo', 0.0)  
            )
            session.add(usuario)
            session.commit()  
            return jsonify({'message': 'Usuario creado exitosamente', 'usuario': usuario.to_dict()}), 201
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    '''
    {
  "nombre": "Juan Perez",
  "correo": "juan@example.com",
  "contraseña": "123456",
  "saldo": 100.5
    }
    '''


@usuario_bp.route('/actualizar', methods=['PUT'])
def update_usuario():
    try:
        data = request.get_json()  
        with SessionLocal() as session:
            usuario_existente = session.query(Usuario).filter_by(id=data['id']).first()
            if usuario_existente:
                usuario_existente.nombre = data['nombre']
                usuario_existente.correo = data['correo']
                usuario_existente.contraseña = data['contraseña']
                usuario_existente.saldo = data['saldo']
                session.commit()  # Guardamos los cambios
                return jsonify({'message': 'Usuario actualizado exitosamente', 'usuario': usuario_existente.to_dict()}), 200
            return jsonify({'message': 'Usuario no encontrado'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    
    '''
    {
  "id": 1,
  "nombre": "Juan Pérez Actualizado",
  "correo": "juan_actualizado@example.com",
  "contraseña": "nueva123",
  "saldo": 200.0
    }

    '''


@usuario_bp.route('/eliminar', methods=['DELETE'])
def delete_usuario():
    try:
        data = request.get_json()  
        with SessionLocal() as session:
            usuario = session.query(Usuario).filter_by(id=data['id']).first()
            if usuario:
                session.delete(usuario)
                session.commit() 
                return jsonify({'message': 'Usuario eliminado exitosamente'}), 200
            return jsonify({'message': 'Usuario no encontrado'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500
    
    '''
    {
  "id": 1
    }

    '''
