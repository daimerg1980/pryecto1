from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, FileField, SelectField,DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    usuario = StringField(' Usuario', validators=[DataRequired(message="Debes llenar este campo")])
    contrasena = PasswordField('Contrasena', validators=[DataRequired(message="Debes llenar este campo")])
    recordar = BooleanField('Recordar Usuario')
    
class EmpleadoForm(FlaskForm):
    id = StringField('Código', validators=[DataRequired(message="Debes llenar este campo")])
    documento =  IntegerField('Documento', validators=[DataRequired(message="Debes llenar este campo")])
    nombre = StringField('Nombre', validators=[DataRequired(message="Debes llenar este campo")])
    apellido = StringField('Apellido', validators=[DataRequired(message="Debes llenar este campo")])
    telefono =  IntegerField('Telefono', validators=[DataRequired(message="Debes llenar este campo")])
    direccion= StringField('Direccion', validators=[DataRequired(message="Debes llenar este campo")])
    correo = StringField('Correo', validators=[DataRequired(message="Debes llenar este campo")])
    fecha_in = DateField(label='Fecha de inicio',format='%d-%m-%Y',validators = [DataRequired('please select startdate')])
    tipo_con=SelectField('Tipo de contraro', choices = [('Contrato de trabajo a término fijo', 'Contrato de trabajo a término fijo'),
     ('Contrato a término indefinido', 'contrato a término indefinido'),('contrato de aprendizaje', 'Contrato de aprendizaje'),
     ('Contrato temporal, ocasional o accidental', 'Contrato temporal, ocasional o accidental')])
    fecha_ter=DateField('Fecha de termino', format='%d/%m/%Y')
    cargo = SelectField('Cargo', choices = [('Super Administrador', 'Super Administrador'),
     ('Administrador', 'Administrador'),('Usuario', 'Usuario')])
    salario=StringField('Salario',validators=[DataRequired(message="Debes llenar este campo")])
    contrasena = StringField('contrasena', validators=[DataRequired(message="Debes llenar este campo")])

class EmpleadoFormAd(FlaskForm):
    id = StringField('Código', validators=[DataRequired(message="Debes llenar este campo")])
    documento =  IntegerField('Documento', validators=[DataRequired(message="Debes llenar este campo")])
    nombre = StringField('Nombre', validators=[DataRequired(message="Debes llenar este campo")])
    apellido = StringField('Apellido', validators=[DataRequired(message="Debes llenar este campo")])
    telefono =  IntegerField('Telefono', validators=[DataRequired(message="Debes llenar este campo")])
    direccion= StringField('Direccion', validators=[DataRequired(message="Debes llenar este campo")])
    correo = StringField('Correo', validators=[DataRequired(message="Debes llenar este campo")])
    fecha_in = DateField(label='Fecha de inicio',format='%d-%m-%Y',validators = [DataRequired('please select startdate')])
    tipo_con=SelectField('Tipo de contraro', choices = [('Contrato de trabajo a término fijo', 'Contrato de trabajo a término fijo'),
     ('Contrato a término indefinido', 'contrato a término indefinido'),('contrato de aprendizaje', 'Contrato de aprendizaje'),
     ('Contrato temporal, ocasional o accidental', 'Contrato temporal, ocasional o accidental')])
    fecha_ter=DateField('Fecha de termino', format='%d/%m/%Y')
    cargo = SelectField('Cargo', choices = [('Administrador', 'Administrador'),('Usuario', 'Usuario')])
    salario=StringField('Salario',validators=[DataRequired(message="Debes llenar este campo")])
    contrasena = StringField('contrasena', validators=[DataRequired(message="Debes llenar este campo")])
   
  
    
class infForm(FlaskForm):
    id_informe= StringField('id_informe', validators=[DataRequired(message="Debes llenar este campo")])
    id_empleado= StringField('id_empleado', validators=[DataRequired(message="Debes llenar este campo")])
    Calificacion= StringField('calificacion', validators=[DataRequired(message="Debes llenar este campo")])
    Retroalimentacion= StringField('Retroalimentacion', validators=[DataRequired(message="Debes llenar este campo")])
