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
    # devuelve una tupla()
    return render_template('index.html', contacts = data)
@app.route('/add_contact',methods=['POST'])
def add_contact():
   if request.method == "POST" :
    fullname = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    
    # cursor ejecuta consultas sql
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO contacts (fullname,phone,email) VALUES(%s,%s,%s)',(fullname,phone,email))
    mysql.connection.commit()
    flash('Contacto Agregado')
    return redirect(url_for('Index'))
# no hace falta marcar el tipo de datos por parametros
@app.route('/edit/<id>')
def get_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * from contacts where id=%s',[id])
    data = cursor.fetchall()
    print("🚀 ~ file: App.py ~ line 44 ~ data", data)
    return render_template('edit-contact.html', singleContac = data[0])

@app.route('/delete/<string:id>')
def delete_contact(id):
    cursor = mysql.connection.cursor()
    # aca paso la consulta con id ={0} que corresponde al indice de la tupla, del dato que vamos a reemplazar 
    # y con format el id lo formateo a string 
    cursor.execute('DELETE from contacts where id={0}'.format(id))
    mysql.connection.commit()
    flash('CONTACTO ELIMINADO')
    return redirect(url_for('Index'))
@app.route('/update_contac/<id>', methods = ['POST'])
def update_contac(id):
    if request.method == "POST":
        fullname = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE contacts
        SET fullname = %s,
            phone = %s,
            email = %s
        WHERE id = %s
    """,(fullname,phone,email,id))
    mysql.connection.commit()
    flash("UPDATE CONTACT")
    # %s es para pasar un STRING
    return redirect(url_for('Index'))

# cada vez que un usuario entre a nuestra raiz ('/') de la app ingresa al slash que le marcamos
if __name__  == '__main__':
    app.run(port= 3000, debug=True)
    # si el archivo que se esta ejecutando es app.py, empieza  ejecutar el servidor
# cada vez que hago cambios dentro del servicor esto lo debub reinicia automaticamente

