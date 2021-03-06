from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('fresh', views.fresh),
    path('popular', views.popular),
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
    path('<int:post_id>/<int:comment_id>/<int:child_id>/answer_child/', views.answer_child),
    path('<int:post_id>/<int:comment_id>/<int:child_id>/answer_child/child_answering/', views.answering_child),
    path('<int:post_id>/<int:comment_id>/<int:parent_id>/', views.childing),
    #link = '//127.0.0.1:8000/main/' + str(post_id)+'/'+str(comment_id)+'/'+str(child_id)+'/'+str(comment2.comment_id )+'/'
    path('<int:post_id>/<int:comment_id>/<int:child_id>/<int:parent_id>/really_child_answering/', views.really_answering)
]