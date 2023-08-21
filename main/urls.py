from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('logout/', views.logout, name='logout'),
        path("room/<str:room_name>/", views.room, name="room"),
        path("write/", views.write, name="write"),
        ]
