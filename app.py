import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from datetime import datetime
from flask import Flask, render_template, jsonify, request, redirect, url_for
from helpdesk.database import db

from helpdesk.models.usuario import Usuario
from helpdesk.models.chamado import Chamado

from helpdesk.controllers.usuario_controller import usuario_bp
from helpdesk.controllers.chamado_controller import chamado_bp

from helpdesk.routers.routers import usuario_bp, chamado_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bravoFortKnox'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Usuario.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(chamado_bp)
app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    app.run(debug=True)
