from flask import Flask
from routes.boleto_routes import boleto_bp
from routes.usuario_routes import usuario_bp
from routes.rifa_dao import rifa_bp
from routes.apuesta_routes import apuesta_bp
from routes.pago_premio_routes import pago_premio_bp
from routes.participacion_apuesta_dao import participacion_apuesta_bp
app = Flask(__name__)


app.register_blueprint(boleto_bp, url_prefix='/boleto')
app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(rifa_bp, url_prefix='/rifa')
app.register_blueprint(apuesta_bp, url_prefix='/apuesta')
app.register_blueprint(pago_premio_bp, url_prefix= '/pago_premio')
app.register_blueprint(participacion_apuesta_bp, url_prefix= '/participacion_apuesta')



if __name__ == '__main__':
    app.run(debug=True)
