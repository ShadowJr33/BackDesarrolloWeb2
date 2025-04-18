from flask import Flask
from routes.boleto_routes import boleto_bp
from routes.usuario_routes import usuario_bp

app = Flask(__name__)


app.register_blueprint(boleto_bp, url_prefix='/boleto')
app.register_blueprint(usuario_bp, url_prefix='/usuario')
if __name__ == '__main__':
    app.run(debug=True)
