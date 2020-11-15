from django.urls import path
from . import views
from django.views.generic import DetailView



app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:pk>', views.detailprogramme, name='detailpro'),
    path('gallery/', views.gallery, name='gallery'),
    path('trainer/', views.trainer, name='trainer'),
    path('pricing/', views.pricing, name='pricing'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>', views.detail, name='detail'),
    path('blog/search', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.loginPage, name='logout'),
    path('register/', views.registerPage, name='register')


]
