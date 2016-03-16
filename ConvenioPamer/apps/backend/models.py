# -*- coding: utf_8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# LISTAS
TIPO_DOCUMENTO_CHOICES = (
    ('1', 'DNI'),
    ('2', 'CE'),
)
TIPO_OPERADOR_CHOICES = (
    ('1', 'MOVISTAR'),
    ('2', 'CLARO'),
    ('3', 'BITEL'),
    ('4', 'ENTEL'),
)
# INSTITUCION
class instInstitucion(models.Model):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    razon_social = models.CharField(max_length=250, blank=True, null=True)
    direccion_fiscal = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    ruc = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)


class instSede(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    ubicacion = models.CharField(max_length=6,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)


class instLocal(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    ubicacion = models.CharField(max_length=6, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)


class instAmbiente(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    local_id = models.ForeignKey(instLocal)
    piso = models.IntegerField()
    nombre = models.CharField(max_length=250, blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)
    capacidad_adicional = models.IntegerField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    is_aula = models.NullBooleanField()
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)


# ICPNA
class icpnaUbigeo(models.Model):
    departamento = models.CharField(max_length=2)
    distrito = models.CharField(max_length=2)
    provincia = models.CharField(max_length=2)
    nombre = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)


class icpnaPersona(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    codigo = models.CharField(max_length=250, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=250, blank=True, null=True)
    apellido_materno = models.CharField(max_length=250, blank=True, null=True)
    nombres = models.CharField(max_length=250, blank=True, null=True)
    tipo_documento = models.CharField(choices=TIPO_DOCUMENTO_CHOICES,max_length=1, default='DNI')
    nro_documento = models.CharField(max_length=250, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    ubigeo = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    referencia_direccion = models.TextField(blank=True, null=True)
    estado_civil = models.CharField(max_length=1, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    grado_academico = models.CharField(max_length=1, blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    img_documento = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)


class icpnaTelefonoPersona(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    persona_id = models.ForeignKey(icpnaPersona)
    numero = models.CharField(max_length=250, blank=True, null=True)
    operador = models.CharField(max_length=1,choices=TIPO_OPERADOR_CHOICES,default=1)
    descriptor = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.persona_id)


class icpnaAlumno(models.Model):
    persona_id = models.ForeignKey(icpnaPersona)
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    clave = models.CharField(max_length=20)
    is_nuevo = models.BooleanField(default=True)
    fecha_inscripcion = models.DateField(blank=True, null=True)
    pago_duplicado = models.BooleanField()
    fecha_duplicado = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    workstation_name = models.CharField(max_length=150, blank=True, null=True)
    workstation_ip = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.persona_id)



class icpnaDocente(User):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    workstation_name = models.CharField(max_length=150, blank=True, null=True)
    workstation_ip = models.CharField(max_length=150, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'icpnaAlumno'


# CURSOS
class acadPrograma(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)



class acadModalidad(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    nombre = models.TextField(max_length=128, blank=True, null=True)
    programa_id = models.ForeignKey(acadPrograma)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)


class acadHorarioTurno(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    modalidad_id = models.ForeignKey(acadModalidad)
    turno = models.CharField(max_length=16, blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.turno)


class acadHorarioTurnoHoras(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    horarioturno_id = models.ForeignKey(acadHorarioTurno)
    inicio = models.TimeField(blank=True, null=True)
    fin = models.TimeField(blank=True, null=True)
    dia = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.inicio)


class acadNivel(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    programa_id = models.ForeignKey(acadPrograma)
    nombre = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)


class acadCurso(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    nivel_id = models.ForeignKey(acadNivel)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)


class acadCalendarioAcademica(models.Model):
    sede_id = models.ForeignKey(instSede)
    institucion_id = models.ForeignKey(instInstitucion)
    anno = models.IntegerField()
    mes = models.IntegerField()
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, max_length=128, blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.mes)


class acadOfertaAcademica(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    curso_id = models.ForeignKey(acadCurso)
    ambiente_id = models.ForeignKey(instAmbiente)
    docente_id = models.ForeignKey(icpnaDocente)
    calendarioacademica_id = models.ForeignKey(acadCalendarioAcademica)
    horarioturno_id = models.ForeignKey(acadHorarioTurno)
    horarioturnohoras_id = models.ForeignKey(acadHorarioTurnoHoras, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.curso_id.nombre,self.horarioturnohoras_id)


class icpnaMatricula(models.Model):
    institucion_id = models.ForeignKey(instInstitucion)
    sede_id = models.ForeignKey(instSede)
    ofertaacademica_id = models.ForeignKey(acadOfertaAcademica)
    alumno_id = models.ForeignKey(icpnaAlumno)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.id)

class icpnaAsistenciaDocente(models.Model):
    ofertaacademica_id = models.ForeignKey(acadOfertaAcademica)
    docente_id = models.ForeignKey(icpnaDocente)
    ingreso_fecha = models.DateField(blank=True, null=True)
    ingreso_hora = models.TimeField(blank=True, null=True)
    salida_fecha = models.DateField(blank=True, null=True)
    salida_hora = models.TimeField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    workstation_name = models.TextField(blank=True, null=True)
    workstation_ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.ofertaacademica_id.curso_id,self.docente_id)
