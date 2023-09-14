from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('logout/', views.logout, name='logout'),
        path("room/<str:room_name>/", views.room, name="room"),
        path("load/<str:room_name>/", views.load_messages, name="load_messages"),
        path("write/", views.write, name="write"),
        ]
