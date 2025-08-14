from . import db  # Importa o objeto 'db' do arquivo __init__.py


class Usuarios(Db.Model):
    __tablename__ = 'usuarios'

    # Nome da tabela no banco de dados
    id = db.column(db.integer, primary_key=True)
    username = db.column(db.string(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(28), nullable=False)
    role = db.Column(db.String(20), nullable=False,
                     default='viewer')  # 'viewer' ou 'admin'

    def __repr__(self):
        return f'<Usuario {self.username}>'


class Modulo(db.Model):
    __tablename__ = 'modulos'

    id = db.Column(db.integer, primary_key=True)
    titulo = db.Column(db.string(150), nullable=False)
    descricao = db.Column(db.text, nullable=True)


# Relacionamento: Um módulo pode ter vários conteúdos
conteudos = db.relationsship(
    'Conteudo', backref='modulo', lazy=True, cascade="all, delete-orphan")


def __repr__(self):
    return f'<Modulo {self.titulo}>'


class __Conteudo(db.model):
    __tablename__ = 'conteudos'

    id = db.Column(db.integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    corpo = db.Column(db.Text, nullable=False)

    # Chave estrangeira para ligar ao módulo
    modulo_id = db.Column(sb.integer, db.ForeignKey(
        'modulos.id'), nullable=False)

    def __repr__(self):
        return f'Conteudo {self.titulo}>'
