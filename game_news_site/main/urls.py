from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dtf', views.dtf_, name='dtf'),
    path('igrm', views.igrm_, name='igrm'),
    path('vg', views.vg_, name='vg'),
    path('<int:post_id>', views.details),
    path('register/', views.register_page),
    path('registrate/', views.register),
    path('<int:post_id>/like/', views.like),
    path('<int:post_id>/dislike/', views.dislike),
    path('<int:post_id>/comment/', views.comment ),
    path('<int:post_id>/comment/commenting/', views.commenting ),
    path('<int:post_id>/<int:comment_id>/answer_comment/', views.anscomment),
    path('<int:post_id>/<int:comment_id>/answer_comment/answering/', views.answering),
]