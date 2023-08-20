from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('logout/', views.index, name='logout'),
        path("room/<str:room_name>/", views.room, name="room"),
        ]
