from django.conf.urls import patterns, include, url

urlpatterns = patterns('ConvenioPamer.apps.backend.views',
	url(r'^$','pamer',name='pamer'),
	url(r'^asistencia_docente/$','asistencia_docente',name='asistencia_docente'),
	url(r'^asistencia_docente_id/(?P<idOfertaAcad>\d+)$', 'asistencia_docente_id', name='asistencia_docente_id'),
	url(r'^asistencia_docente_ingreso/(?P<idAsistenciaDocente>\d+)$', 'asistencia_docente_ingreso', name='asistencia_docente_ingreso'),
	url(r'^asistencia_docente_salida/(?P<idAsistencia>\d+)$', 'asistencia_docente_salida', name='asistencia_docente_salida'),
)
