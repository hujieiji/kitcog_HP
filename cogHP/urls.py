from django.urls import path

from . import views

urlpatterns = [
    path('', views.top, name="top"),
    path('achivements/', views.achivements, name="achivements"),
    path('recruiting/', views.recruiting_index, name='index'),
    path('recruiting/<int:recruiting_id>/', views.recruiting_detail, name='detail')
]