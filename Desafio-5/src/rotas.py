from __main__ import app
from flask import Flask, render_template, request
import conexao

@app.route("/")
@app.route("/home")
def index():
  return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
  return render_template("quemsomos.html")

@app.route("/contato", methods = ["GET", "POST"])
def contatos():
  if request.method == "POST":
    form = request.form
    conexao.insere_usuario(form)
    return render_template("contato.html")
  else:
    return render_template("contato.html")

@app.route("/usuario")
def usuarios():
  usuarios = conexao.retorna_usuarios()
  return render_template("usuario.html", usuarios = usuarios)