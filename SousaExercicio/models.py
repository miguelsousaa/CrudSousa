from database import db

class Planos(db.Model):
    
    __tablename__= "Planos"
    id_plano = db.Column(db.Integer, primary_key = True)
    nome_plano = db.Column(db.String(100))
    cobertura = db.Column(db.String(100))
    valor_mensal = db.Column(db.Float(10,2))

    def __init__(self, nome_plano, cobertura, valor_mensal):
        self.nome_plano = nome_plano
        self.cobertura = cobertura
        self.valor_mensal = valor_mensal

    def __repr__(self):
        return "<Plano {}>".format(self.nome_plano)