
from flask_mysqldb import MySQL
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_nomina'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()  
        if valid_credentials(username, password):
            return redirect(url_for('panel_p'))
        else:
            flash('Credenciales incorrectas', 'danger')
            error_message = 'Credenciales incorrectas'
    else:
        error_message = '' 

    return render_template('login.php', error_message=error_message)


@app.route('/liquidacion')
def liquidacion():
    return render_template('liquidacion.html')



def valid_credentials(username, password):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s', (username, password))
        user_data = cur.fetchone()

        if user_data:
            return True
        else:
            return False

    except mysql.connetor.Error as e:
        print("Error de base de datos:", str(e))
        return False

    finally:
        if cur is not None:
            cur.close()

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/panel_p')
def panel_p():
    return render_template('panel_p.html')

@app.route('/man-trabajadores')
def man_trabajadores():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM empleados')
    data = cur.fetchall()
    print(data)
    return render_template('mant-trabajadores.html', empleados = data)

@app.route('/otra_pagina')
def otra_pagina():
    return render_template('cargar-datos.html')

@app.route('/add_contact', methods = ['POST'])
def add_contact():    
    if request.method == 'POST':
        num_doc     = request.form['num_doc']
        tipo_doc    = request.form['tipo_doc']
        names       = request.form['names']
        apellidos   = request.form['apellidos']
        telefono    = request.form['telefono']
        direccion   = request.form['direccion']
        f_ingreso   = request.form['f_ingreso']
        cargo       = request.form['cargo']
        departamento= request.form['departamento']
        salario     = request.form['salario']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO empleados (num_doc, tipo_doc, nombres, apellidos, telefono, direccion, f_ingreso, cargo, departamento, salario) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (num_doc, tipo_doc, names, apellidos, telefono, direccion, f_ingreso, cargo, departamento, salario))
        mysql.connection.commit()
        return redirect(url_for('man_trabajadores'))
        

@app.route('/edit/<id>')
def get_empleado(id):    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM empleados WHERE id = %s', [id])
    data = cur.fetchall()
    return render_template('edit-trabajadores.html', empleado = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_empleado(id):
    if request.method == 'POST':
        num_doc     = request.form['num_doc']
        tipo_doc    = request.form['tipo_doc']
        names       = request.form['names']
        apellidos   = request.form['apellidos']
        telefono    = request.form['telefono']
        direccion   = request.form['direccion']
        f_ingreso   = request.form['f_ingreso']
        cargo       = request.form['cargo']
        departamento= request.form['departamento']
        salario     = request.form['salario']
    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE empleados
                SET num_doc = %s,
                tipo_doc    = %s,
                nombres     = %s,
                apellidos   = %s,
                telefono    = %s,
                direccion   = %s,
                f_ingreso   = %s,
                cargo       = %s,  
                departamento= %s,
                salario     = %s     
                WHERE id    = %s
                """, (num_doc, tipo_doc, names, apellidos, telefono, direccion, f_ingreso, cargo, departamento, salario, id))
    mysql.connection.commit()
    flash('Person Update Sucessfully')
    return redirect(url_for('man_trabajadores'))

        
@app.route('/delete/<string:id>')
def delete_contact(id):    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM empleados where id = {0}'.format(id))
    mysql.connection.commit()
    flash('Trabajador Eliminado')
    return redirect(url_for('man_trabajadores'))

#MANTENIMIENTO NOMINAS

@app.route('/man-nominas')
def man_nominas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM nomina')
    data = cur.fetchall()
    print(data)
    return render_template('mant-nominas.html', nominas = data)

@app.route('/editar/<id>')
def get_nomina(id):    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM nomina WHERE id = %s', [id])
    data = cur.fetchall()
    return render_template('edit-nominas.html', nomina = data[0])

@app.route('/update_/<id>', methods = ['POST'])
def update_nomina(id):
    if request.method == 'POST':
        num_doc     = request.form['num_doc']
        tipo_doc    = request.form['tipo_doc']
        names       = request.form['names']
        apellidos   = request.form['apellidos']
        f_ingreso   = request.form['f_ingreso']
        cargo       = request.form['cargo']
        salario     = request.form['salario']
        sueldoneto = request.form['sueldoneto']
        horas_extras = request.form['horas_extras']
        precio_horas_extras = request.form['precio_horas_extras']
        pago_horas_extras = request.form['pago_horas_extras']
        fecha_creacion = request.form['fecha_creacion']
    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE nomina
                SET num_doc = %s,
                tipo_doc    = %s,
                nombres     = %s,
                apellidos   = %s,
                f_ingreso   = %s,
                cargo       = %s,  
                salario     = %s,
                sueldobruto = %s,
                horas_extras= %s,
                precio_horas_extras=%s,
                pago_horas_extras=%s,
                fecha_creacion=%s
                WHERE id    = %s
                """, (num_doc, tipo_doc, names, apellidos, f_ingreso, cargo, salario, sueldoneto, horas_extras, precio_horas_extras, pago_horas_extras, fecha_creacion , id))
    mysql.connection.commit()
    return redirect(url_for('man_nominas'))


@app.route('/borrar/<string:id>')
def delete_nomina(id):    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM nomina WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Nomina Eliminada')
    return redirect(url_for('man_nominas'))


#MANTENIMIENTO USUARIO

@app.route('/man-usuarios')
def man_usuarios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data = cur.fetchall()
    print(data)
    return render_template('mant-usuario.html', usuarios = data)

@app.route('/page_user')
def page_user():
    return render_template('cargar-usuario.html')

@app.route('/add_user', methods = ['POST'])
def add_user():    
    if request.method == 'POST':
        names       = request.form['names']
        apellidos   = request.form['apellidos']
        usuario     = request.form['usuario']
        contraseña  = request.form['contraseña']
        id_rol      = request.form['id_rol']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (nombres, apellidos, usuario, contraseña,id_rol) VALUES (%s,%s,%s,%s)',
                    (names, apellidos, usuario, contraseña))
        mysql.connection.commit()
        flash('User Added Sucess')
        return redirect(url_for('man_usuarios'))

@app.route('/editar_/<id>')
def get_usuario(id):    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = %s', [id])
    data = cur.fetchall()
    return render_template('edit-usuario.html', usuario = data[0])

@app.route('/update-/<id>', methods = ['POST'])
def update_user(id):
    if request.method == 'POST':
        names       = request.form['names']
        apellidos   = request.form['apellidos']
        usuario     = request.form['usuario']
        contraseña  = request.form['contraseña']
    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE usuarios
                SET nombres = %s,
                apellidos   = %s,
                usuario     = %s,
                contraseña  = %s     
                WHERE id    = %s
                """, (names, apellidos, usuario, contraseña, id))
    mysql.connection.commit()
    flash('User Update Sucessfully')
    return redirect(url_for('man_usuarios'))

@app.route('/delete_/<string:id>')
def delete_usuario(id):    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Usuario Eliminado')
    return redirect(url_for('man_usuarios'))


@app.route('/reportesU')
def reportesU():
    return render_template('reportesusuario.html')


if __name__ == '__main__':
    app.run(debug=True)
