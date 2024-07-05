from django.urls import path
from . import views
from .views import  welcome_view

urlpatterns = [
    path('api/hello/', views.VisitorsView.as_view(), name='visitor'),
    path('', welcome_view, name='welcome')
]
