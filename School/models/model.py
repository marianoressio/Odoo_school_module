from odoo import models, fields


class ProfesorRecord(models.Model):

    _name = "profesor.profesor"
    nombre = fields.Char(string='Nombre', required=True)
    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
    foto = fields.Binary(string='Foto')
    edad = fields.Integer(string='Edad')
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Género')
    nacionalidad = fields.Many2one('res.country', string='Nacionalidad')
    profile = fields.Text(string='Perfil')
    subject_ids = fields.One2many('asignatura.asignatura', string='Asignatura')


class AsignaturaRecord(models.Model):

    _name = "asignatura.asignatura"
    nombre = fields.Char(string='Nombre', required=True)
    temas = fields.Integer(string='Temas')
    tipo = fields.Selection([('c', 'Ciencias'), ('l', 'Letras'), ('i', 'Idiomas'), ('o', 'Otro')], string='Tipo')
    credit = fields.Integer(string='Créditos')
    max_students = fields.Integer(string='Max Alumnos')
    active = fields.Boolean(string='Activo')
    student_id = fields.Many2many('alumno.alumno', string='Alumno')
    teacher_id = fields.Many2one('profesor.profesor', string='Profesor')


class AlumnoRecord(models.Model):

    _name = "alumno.alumno"
    nombre = fields.Char(string='Nombre', required=True)
    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
    foto = fields.Binary(string='Foto')
    edad = fields.Integer(string='Edad')
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Género')
    nacionalidad = fields.Many2one('res.country', string='Nacionalidad')
    final_exam_grade = fields.Float(string='Calificación Exámen Final')
    subject_ids = fields.Many2many('asignatura.asignatura', string='Asignatura')