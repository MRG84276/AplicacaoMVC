from datetime import datetime
from database import db


class Chamado(db.Model):
    __tablename__ = 'chamado'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    prioridade = db.Column(db.String(20), default='Média', nullable=False)  
    status = db.Column(db.String(20), default='Aberto', nullable=False)     
    tecnico = db.Column(db.String(80), nullable=True)                       
    data_abertura = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'prioridade': self.prioridade,
            'status': self.status,
            'tecnico': self.tecnico,
            'data_abertura': self.data_abertura.isoformat() if self.data_abertura else None,
            'usuario_id': self.usuario_id
        }
