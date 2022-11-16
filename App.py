from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
# CONECTION
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'python_flask'
mysql = MySQL(app)

# SESSION -  guardar dentro de la memoria de la app.
app.secret_key = 'mysecretkey'
# decorador @
@app.route('/')
#  lo manejamos con una funcion 
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute('select * from contacts')
    data = cursor.fetchall()
    print(data)
    # devuelve una tupla()
    return render_template('index.html')
@app.route('/add_contact',methods=['POST'])
def add_contact():
   if request.method == "POST" :
    fullname = request.form['name']
    print("🚀 ~ file: App.py ~ line 20 ~ fullname", fullname)
    phone = request.form['phone']
    print("🚀 ~ file: App.py ~ line 22 ~ phone", phone)
    email = request.form['email']
    print("🚀 ~ file: App.py ~ line 24 ~ email", email)
    
    # cursor ejecuta consultas sql
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO contacts (fullname,phone,email) VALUES(%s,%s,%s)',(fullname,phone,email))
    mysql.connection.commit()
    flash('Contacto Agregado')
    return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return 'edit'
@app.route('/delete')
def delete_contact():
    return 'delete'


# cada vez que un usuario entre a nuestra raiz ('/') de la app ingresa al slash que le marcamos
if __name__  == '__main__':
    app.run(port= 3000, debug=True)
    # si el archivo que se esta ejecutando es app.py, empieza  ejecutar el servidor
# cada vez que hago cambios dentro del servicor esto lo debub reinicia automaticamente

