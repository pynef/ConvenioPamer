from ConvenioPamer.decorators import backend_login
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from ConvenioPamer.apps.backend.models import acadOfertaAcademica
from ConvenioPamer.apps.backend.models import icpnaAsistenciaDocente
from ConvenioPamer.apps.backend.models import icpnaDocente
from datetime import date
import datetime

@login_required(login_url="login")
# @backend_login
def pamer(request):
    # user = User.objects.get(id=request.user.id)
    cntxt = {
    # user : 'user',
    }
    return render(request,'backend/index.html')


@login_required(login_url="login")
def asistencia_docente(request):
    # user = User.objects.get(id=request.user.id)
    cursos = acadOfertaAcademica.objects.filter(docente_id=request.user.id)
    print cursos
    cntxt = {
        # user : 'user',
        'cursos' : cursos,
        }
    return render(request,'backend/pamer_asistencia_docente.html',cntxt)


@login_required(login_url="login")
def asistencia_docente_id(request, idOfertaAcad):
    # user = User.objects.get(id=request.user.id)
    ofertaAcademica = acadOfertaAcademica.objects.get(id=idOfertaAcad)
    cursos = acadOfertaAcademica.objects.filter(docente_id=request.user.id)
    i = icpnaAsistenciaDocente.objects.filter
    try:
        ingreso = icpnaAsistenciaDocente.objects.get(ingreso_fecha=date.today(),docente_id=request.user.id,ofertaacademica_id=idOfertaAcad)
        # salida = icpnaAsistenciaDocente.objects.get(ingreso_fecha=date.today(),docente_id=request.user.id,ofertaacademica_id=idOfertaAcad,salida_hora=None)
    except:
        ingreso = None
        salida = None
    print "asistencia_docente_id"
    print date.today()
    print ingreso
    cntxt = {
        # user : 'user',
        'cursos' : cursos,
        'ofertaAcademica' : ofertaAcademica,
        'ingreso' : ingreso,
        # 'salida' : salida,
        }
    return render(request,'backend/pamer_asistencia_docente_detalle.html',cntxt)


@login_required(login_url="login")
def asistencia_docente_ingreso(request,idAsistenciaDocente):
    asistencia = icpnaAsistenciaDocente.objects.create(
    ofertaacademica_id=acadOfertaAcademica.objects.get(id=idAsistenciaDocente),
    docente_id = icpnaDocente.objects.get(id=request.user.id),
    ingreso_fecha = date.today(),
    ingreso_hora  = datetime.datetime.time(datetime.datetime.now()),
    )
    print asistencia
    # return HttpResponseRedirect(reverse('asistencia_docente_id' idAsistenciaDocente))
    return HttpResponseRedirect(reverse('asistencia_docente_id',args=[idAsistenciaDocente]))


@login_required(login_url="login")
def asistencia_docente_salida(request,idAsistencia):
    salida = icpnaAsistenciaDocente.objects.get(pk=idAsistencia)
    salida.salida_fecha = date.today()
    salida.salida_hora  = datetime.datetime.time(datetime.datetime.now())
    salida.save()
    print salida.ofertaacademica_id.id
    return HttpResponseRedirect(reverse('asistencia_docente_id',args=[salida.ofertaacademica_id.id]))
