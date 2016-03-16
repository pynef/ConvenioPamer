from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('ConvenioPamer.apps.backend.urls')),
    # url(r'^media/(?P<path>.*)$','django.views.static.serve',
    # 			{'document_root':settings.MEDIA_ROOT,}),
    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name':'registration/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
]
# urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
#         (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
# )
