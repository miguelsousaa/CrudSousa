from flask import *
from database import db
from flask_migrate import Migrate
from models import Planos

app = Flask(__name__)
app.config["SECRET_KEY"] = "Lu1444444Th3Pr3s1d3nt333S0u64Ch3Gu3v4r4"

# drive://usuario:senha@servidor/banco_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/planosflask" 
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/planos")
def planos():
    p = Planos.query.all()
    return render_template("planos.html", dados=p)

@app.route("/planos/add")
def planos_add():
    return render_template("planos_add.html")

@app.route("/planos/save", methods=["POST"])
def save():
    nome_plano = request.form.get("nome")
    cobertura = request.form.get("cobertura")
    valor_mensal = request.form.get("valor")
    if nome_plano and cobertura and valor_mensal:
        planos = Planos(nome_plano, cobertura, valor_mensal)
        db.session.add(planos)
        db.session.commit()
        flash("Plano cadastrado com sucesso!!!")
        return redirect('/planos')
    else:
        flash("ERRO!! Preencha todos os campos")
        return redirect('/planos/add')
    
@app.route("/planos/remove/<int:id>")
def planos_remove(id):
    planos = Planos.query.get(id)
    if planos:
        db.session.delete(planos)
        db.session.commit()
        flash("Plano removido com sucesso!!!")
        return redirect("/planos")
    else:
        flash("OPS... Caminho Incorreto!!")
        return redirect("/planos")

@app.route("/planos/edit/<int:id>")
def planos_edit(id):
    try:
        planos = Planos.query.get(id)
        return render_template("planos_edit.html", dados=planos)
    except:
        flash("Plano Inválido")
        return redirect("/planos")
    
@app.route("/planos/editsave", methods=["POST"])
def planos_edit_save():
    id_plano = request.form.get("id")
    nome_plano = request.form.get("nome")
    cobertura = request.form.get("cobertura")
    valor_mensal = request.form.get("valor")

    if id_plano and nome_plano and cobertura and valor_mensal:
        plano = Planos.query.get(id)
        plano.nome = nome_plano
        plano.cobertura = cobertura
        plano.valor = valor_mensal
        db.session.commit()
        flash("Dados alterados com sucesso!!!")
        return redirect("/planos")
    else:
        flash("Por favor, Preencha todas as informações!!")
        return redirect("/planos/edit")

if __name__ == '__main__':
    app.run()