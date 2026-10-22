from django.urls import path
from . import views
urlpatterns=[
    path('', views.home, name='home'),
    path('admission/', views.admission, name='admission'),
    path('courses/', views.courses, name='courses'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
]