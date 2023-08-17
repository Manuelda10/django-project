from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, 'users')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginView.as_view()), # If we use users/login it generates an error
    path('logout/', views.LogoutView.as_view()),
    path('user/', views.UserView.as_view())
]