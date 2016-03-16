from django.contrib import admin

#institucion
from ConvenioPamer.apps.backend.models import instInstitucion
from ConvenioPamer.apps.backend.models import instSede
from ConvenioPamer.apps.backend.models import instLocal
from ConvenioPamer.apps.backend.models import instAmbiente
from ConvenioPamer.apps.backend.models import icpnaUbigeo
admin.site.register(icpnaUbigeo)
admin.site.register(instInstitucion)
admin.site.register(instSede)
admin.site.register(instLocal)
admin.site.register(instAmbiente)

#persona
from ConvenioPamer.apps.backend.models import icpnaPersona
from ConvenioPamer.apps.backend.models import icpnaTelefonoPersona
from ConvenioPamer.apps.backend.models import icpnaAlumno
from ConvenioPamer.apps.backend.models import icpnaDocente
admin.site.register(icpnaPersona)
admin.site.register(icpnaTelefonoPersona)
admin.site.register(icpnaAlumno)
admin.site.register(icpnaDocente)


#academico
from ConvenioPamer.apps.backend.models import acadCalendarioAcademica
from ConvenioPamer.apps.backend.models import acadPrograma
from ConvenioPamer.apps.backend.models import acadNivel
from ConvenioPamer.apps.backend.models import acadCurso
from ConvenioPamer.apps.backend.models import acadModalidad
from ConvenioPamer.apps.backend.models import acadHorarioTurno
from ConvenioPamer.apps.backend.models import acadHorarioTurnoHoras
from ConvenioPamer.apps.backend.models import acadOfertaAcademica

admin.site.register(acadCalendarioAcademica)
admin.site.register(acadPrograma)
admin.site.register(acadNivel)
admin.site.register(acadCurso)
admin.site.register(acadModalidad)
admin.site.register(acadHorarioTurno)
admin.site.register(acadHorarioTurnoHoras)
admin.site.register(acadOfertaAcademica)


#asistencia
from ConvenioPamer.apps.backend.models import icpnaAsistenciaDocente
admin.site.register(icpnaAsistenciaDocente)

