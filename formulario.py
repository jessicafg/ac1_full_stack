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
    nome = request.form['nome'] 
    cpf = request.form['cpf'] 
    endereco = request.form['endereco'] 
    if nome and cpf and endereco:
        conn = mysql.connect() 
        cursor = conn.cursor() 
        cursor.execute('insert int formulario_mvc (user_name, number_cpf, user_adress) VALUES (%s, %s, %s)', (nome,cpf,endereco))
        conn.comit() 
    return render_template('formulario.html') 

@app.route('/listar', methods=['POST', GET])
def listar():
        conn = mysql.connect() 
        cursor = conn.cursor()
        cursor.execute('select (user_name, number_cpf, user_adress from formulario')
        data = cursor.fetchall()
        conn.comit()
        return render_template('lista.html', datas=data)
        if __name__=="__main__":
            port = int(os.environ.get("PORT",5008))
            app.run(host='0.0.0.0', port=port)