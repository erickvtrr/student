from . import db  # Importa o objeto 'db' do arquivo __init__.py


class Usuario(db.Model):
    __tablename__ = 'usuarios'  # Nome da tabela no banco de dados

    # CORREÇÃO: 'Column' e 'Integer' com 'C' e 'I' maiúsculos.
    id = db.Column(db.Integer, primary_key=True)

    # CORREÇÃO: 'Column' e 'String' com 'C' e 'S' maiúsculos.
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='viewer')

    def __repr__(self):
        return f'<Usuario {self.username}>'


class Modulo(db.Model):
    __tablename__ = 'modulos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    conteudos = db.relationship(
        'Conteudo', backref='modulo', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Modulo {self.titulo}>'


class Conteudo(db.Model):
    __tablename__ = 'conteudos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    modulo_id = db.Column(db.Integer, db.ForeignKey(
        'modulos.id'), nullable=False)

    def __repr__(self):
        return f'<Conteudo {self.titulo}>'
