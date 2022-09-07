import os
from flask import Flask, request, abort, render_template
from Flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(_name_)

#mySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYQSL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYQSL_DATABASE_DB'] = 'teste'
app.config['MYQSL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def mains():
    return render_template('formulario.html')


@app.route('/gravar', methods=['POST', GET])
def gravar():
    nome = request.form['nome'] #lê o campo nome
    email = request.form['email'] #lê o campo email
    senha = request.form['senha'] #lê o campo senha
    if nome and email and senha: #valida se nenhum dos campos é nulo
        conn = mysql.connect() #se não for nulo, estabelece uma conexão com o banco
        cursor = conn.cursor() #cria uma sessão de comunicação com o banco de dados
        #comando insert insere os dados do formulário no banco de dados. %s significa que os campos são strings
        cursor.execute('insert int formulario_mvc (user_name, user_username, user_password) VALUES (%s, %s, %s)', (nome,email,senha))
        conn.comit() #para executar o comando
    return render_template('formulario.html') #retorno da comunicação

@app.route('/listar', methods=['POST', GET])
def listar():
        conn = mysql.connect() #estabelece uma conexão com o banco
        cursor = conn.cursor() #cria uma sessão de comunicação com o banco de dados
        cursor.execute('select user_name, user_username, user_password from formulario') #roda o comando para saber os dados
        data = cursor.fetchall() #recuperação de dados e atribui a variável data
        conn.comit() #para executar o comando
    return render_template('lista.html', datas=data) #retorno da comunicação