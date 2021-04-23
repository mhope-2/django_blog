from django.urls import path
from user import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name="login"),
    path('login/', views.LoginView.as_view(), name='login'),
]



