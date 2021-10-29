import os
from flask.helpers import flash
from werkzeug.datastructures import IfRange
from werkzeug.utils import secure_filename
from forms.forms import *
from flask.logging import * 
from flask import Flask, render_template, url_for, redirect, jsonify, request, session
from db import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key= os.urandom(24)


@app.route('/')
def index():
    return render_template('index.html') 
    

@app.route('/superAdmin')
def superAdmin():  
    if 'user' in session:        
        sql = "SELECT * FROM empleado"
        
        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        empleado = cursorObj.fetchall()
        print(empleado)
        return render_template('superAdmin.html', empleado=empleado)
    else:
        return redirect(url_for('Login'))

@app.route('/administrador')
def administrador():  
    if 'user' in session:        
      
        sql = "SELECT * FROM empleado WHERE Cargo != 'Super Administrador' "
        
        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        empleado = cursorObj.fetchall()
        print(empleado)
        return render_template('administrador.html', empleado=empleado)
    else:
        return redirect(url_for('Login'))

@app.route('/empleado') 
def empleado():  
    if 'user' in session:        
        sql = "SELECT * FROM iNFORME"
        
        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        empleado = cursorObj.fetchall()
        print(empleado)
        return render_template('empleado.html', empleado=empleado)
    else:
        return redirect(url_for('Login'))



""" Buscar empleado """
  
@app.route('/editar_empleado', methods=['GET', 'POST'])
def editar_empleado():

    id = request.args.get('id')    
    if request.method == 'GET':
        form = EmpleadoForm()        
        sql = f'SELECT * FROM empleado WHERE Id_Empleado = {id}'
        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        empleado= cursorObj.fetchall()[0]
        return render_template('editar_empleado.html', form=form, empleado = empleado)

    if request.method == 'POST':
        id = request.form['id']
        documento = request.form['documento']
        nombre = request.form['nombre']
        apellido= request.form['apellido']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        correo = request.form['correo']
        fecha_in=request.form['fecha_in']
        tipo_con=request.form['tipo_con']
        fecha_ter=request.form['fecha_ter']
        cargo=request.form['cargo']
        salario=request.form['salario']
       
      
        db = get_db()
        sql = 'UPDATE empleado SET Id_user = ?, Nombre = ?, Apellidos = ?, Telefono = ?, Direccion = ?, Correo = ?,Fecha_Ingreso  = ?,Tipo_contrato = ?,Fecha_termino = ?,Cargo = ?,Salario = ? WHERE Id_Empleado = ?'
        result = db.execute(sql, (documento, nombre, apellido, telefono, direccion, correo,fecha_in,tipo_con,fecha_ter, cargo,salario,id)).rowcount
        db.commit()
        if result > 0:
            flash('Registro editado correctamente')
        else:
            flash('No se pudo editar el registro')             
        return redirect(url_for('superAdmin'))

@app.route('/editar_empleadoAd', methods=['GET', 'POST'])
def editar_empleadoAd():

    id = request.args.get('id')    
    if request.method == 'GET':
        form = EmpleadoFormAd()        
        sql = f'SELECT * FROM empleado WHERE Id_Empleado = {id}'
        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        empleado= cursorObj.fetchall()[0]
        return render_template('editar_empleadoAd.html', form=form, empleado = empleado)

    if request.method == 'POST':
        id = request.form['id']
        documento = request.form['documento']
        nombre = request.form['nombre']
        apellido= request.form['apellido']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        correo = request.form['correo']
        fecha_in=request.form['fecha_in']
        tipo_con=request.form['tipo_con']
        fecha_ter=request.form['fecha_ter']
        cargo=request.form['cargo']
        salario=request.form['salario']
       
      
        db = get_db()
        sql = 'UPDATE empleado SET Id_user = ?, Nombre = ?, Apellidos = ?, Telefono = ?, Direccion = ?, Correo = ?,Fecha_Ingreso  = ?,Tipo_contrato = ?,Fecha_termino = ?,Cargo = ?,Salario = ? WHERE Id_Empleado = ?'
        result = db.execute(sql, (documento, nombre, apellido, telefono, direccion, correo,fecha_in,tipo_con,fecha_ter, cargo,salario,id)).rowcount
        db.commit()
        if result > 0:
            flash('Registro editado correctamente')
        else:
            flash('No se pudo editar el registro')             
        return redirect(url_for('administrador'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        emp = request.form['buscar']
        sql = f'SELECT * FROM empleado WHERE Nombre LIKE "%{emp}%"'
        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        empleado = cursorObj.fetchall()
        print(empleado)
        return render_template('superAdmin.html', empleado=empleado)




""" Eliminar el empleado """
@app.route('/deleteEmp', methods=['GET', 'POST'])
def deleteEmp():
   
    id = request.args.get('id')
    sql = 'DELETE FROM empleado WHERE Id_Empleado = ?'
    db = get_db()
    
    result = db.execute(sql,(id,)).rowcount
    if result > 0:
        flash('Empleado eliminado exitosamente')
    else:
        flash('No se pudo eliminar el empleado')        
    db.commit()
    db.close()    
    return redirect(url_for('superAdmin'))






@app.route('/registEmp', methods=['GET','POST'])
def registEmp():


   

    form = EmpleadoForm()
    if request.method == 'POST':
        
        documento = request.form['documento']
        nombre = request.form['nombre']
        apellido= request.form['apellido']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        correo = request.form['correo']
        fecha_in=request.form['fecha_in']
        tipo_con=request.form['tipo_con']
        fecha_ter=request.form['fecha_ter']
        cargo=request.form['cargo']
        salario=request.form['salario']
        contrasena = request.form['contrasena']
        contrasenaHash = generate_password_hash(contrasena)
        db = get_db()
        db.execute('INSERT INTO empleado (Id_user, Nombre, Apellidos, Telefono, Direccion, Correo,Fecha_Ingreso,Tipo_contrato,Fecha_Termino,Cargo,Salario,Contrasena) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (documento, nombre, apellido, telefono, direccion, correo,fecha_in,tipo_con,fecha_ter, cargo,salario,contrasenaHash))
        db.commit()
        return redirect(url_for("superAdmin"))
    return render_template('registEmp.html',form=form)


    
@app.route('/registEmpAd', methods=['GET','POST'])
def registEmpAd():


   

    form = EmpleadoFormAd()
    if request.method == 'POST':
        
        documento = request.form['documento']
        nombre = request.form['nombre']
        apellido= request.form['apellido']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        correo = request.form['correo']
        fecha_in=request.form['fecha_in']
        tipo_con=request.form['tipo_con']
        fecha_ter=request.form['fecha_ter']
        cargo=request.form['cargo']
        salario=request.form['salario']
        contrasena = request.form['contrasena']
        contrasenaHash = generate_password_hash(contrasena)
        db = get_db()
        db.execute('INSERT INTO empleado (Id_user, Nombre, Apellidos, Telefono, Direccion, Correo,Fecha_Ingreso,Tipo_contrato,Fecha_Termino,Cargo,Salario,Contrasena) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (documento, nombre, apellido, telefono, direccion, correo,fecha_in,tipo_con,fecha_ter, cargo,salario,contrasenaHash))
        db.commit()
        return redirect(url_for("administrador"))
    return render_template('registEmpAd.html',form=form)



@app.route('/busInf', methods=['GET', 'POST'])
def busInf():
    if request.method == 'POST':
      
        inf = request.args.get('id')
        sql = f' SELECT Calificacion,Retroalimentacion FROM iNFORME WHERE Id_informe LIKE "{inf}"'
        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        informe= cursorObj.fetchall()
        print(informe)
        return render_template('empleado.html', informe=informe)

 
@app.route('/regisInf', methods=['GET','POST'])
def regisInf():

     
    form = infForm()
     
    if request.method == 'POST':
        
         
        id_empleado= request.form['id_empleado']
        Calificacion= request.form['Calificacion']
        Retroalimentacion= request.form['Retroalimentacion']
    
        db = get_db()
        db.execute('INSERT INTO iNFORME  ( Id_empleado,Calificacion, Retroalimentacion) VALUES (?,?,?)', (id_empleado,Calificacion,Retroalimentacion))
        db.commit()      
        return redirect(url_for("superAdmin"))
    return render_template('regisInf.html',form=form)




@app.route('/Login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if(form.validate_on_submit()):
        usuario = form.usuario.data
        contrasena = form.contrasena.data

        sql = f'SELECT * FROM empleado WHERE empleado.Nombre = "{usuario}" '
        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        empleado = cursorObj.fetchall()  
    
        if len(empleado) > 0:
            contrasenaHash = empleado[0][12]
            if check_password_hash(contrasenaHash, contrasena):
                session.clear()
                session['id'] = empleado[0][0]
                session['user'] = empleado[0][2]
                session['apellido'] = empleado[0][3]
                session['cedula'] = empleado[0][1]
                session['telefono'] = empleado[0][4]
                session['correo'] = empleado[0][6]
                session['fecha_in'] = empleado[0][7]
                session['tipo_con'] = empleado[0][8]
                session['fecha_ter'] = empleado[0][9]
                session['salario'] = empleado[0][11]
                session['password'] = contrasenaHash                
                session['rol'] = empleado[0][10]
               
                if empleado[0][10] == "Super Administrador":               
                    return redirect(url_for('superAdmin'))
                elif empleado[0][10] == "Administrador":
                    return redirect(url_for('administrador'))
                else:
                    return redirect(url_for('empleado'))
            else:
                flash('Clave incorrecta')
                return redirect(url_for('Login'))           
        else:
            flash('El usuario ingresado no existe')
            return redirect(url_for('Login'))
    return render_template('Login.html', form=form)

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('Login'))  
