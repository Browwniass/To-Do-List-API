from django.urls import path, include
from users import views

urlpatterns = [
    path('users/reg/', views.RegistrationView.as_view(), name='registration')
]