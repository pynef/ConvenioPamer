#-*- coding:utf-8 -*-
from django.contrib.auth.models import User,Group
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

def backend_login(view_func):
    def wrap(request, *args, **kwargs):
        is_dir = request.user.groups.filter(name='docente').count()
        if request.user.is_authenticated() and is_dir :
            return view_func( request=request,*args, **kwargs )
        return HttpResponseRedirect(reverse('login'))
    wrap.__doc__ = view_func.__doc__
    wrap.__dict__ = view_func.__dict__
    return wrap
