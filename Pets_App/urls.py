from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('',homepage,name='home' ),
    path('foundpetslist',foundlist,name='foundlist' ),
    path('addlostpet/',addlost,name='addlost' ),
    path('addfoundpet/',addfound,name='addfound' ),
    path('lostpetslist/',lostlist,name='lostlist' ),
    path('Commentpetslist/',Commentlist,name='Commentlist' ),
    path('postpetslist/',postlist,name='postlist' ),
    path('detail/<int:post_id>/',detailpost,name='detailpost' ),
    path('addcomment/', addcomment, name='addcomment'),
    path('lostbyuser/', lostbyuser, name='lostbyuser'),
    path('foundbyuser/', foundbyuser, name='foundbyuser'),
    path('addpost/', addpost, name='addpost'),

]