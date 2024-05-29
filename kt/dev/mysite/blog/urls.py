from django.urls import path, include
from . import views

urlpatterns = [
    path('test1/', views.test1), 
    path('test2/<id>/', views.test2), # <>은 데이터를 동적으로 받겠다는 의미
]
