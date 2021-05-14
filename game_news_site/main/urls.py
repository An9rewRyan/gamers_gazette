from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dtf', views.dtf_, name='dtf'),
    path('igrm', views.igrm_, name='igrm'),
    path('vg', views.vg_, name='vg'),
]