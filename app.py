from datetime import datetime
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bravoFortKnox'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Usuario.db' 

db = SQLAlchemy(app) 


class Usuario(db.Model): 
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    setor = db.Column(db.String(80), nullable=False)

    chamados = db.relationship('Chamado', backref='usuario', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'setor': self.setor
        }


class Chamado(db.Model):
    __tablename__ = 'chamado'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    prioridade = db.Column(db.String(20), default='Média', nullable=False)  
    status = db.Column(db.String(20), default='Aberto', nullable=False)     
    tecnico = db.Column(db.String(80), nullable=True)                       
    data_abertura = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    

    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'prioridade': self.prioridade,
            'status': self.status,
            'tecnico': self.tecnico,
            'data_abertura': self.data_abertura.isoformat(),
            'usuario_id': self.usuario_id
        }


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
