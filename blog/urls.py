from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.CreateBlogView.as_view(), name='create'),
    path('<int:id>/', views.PostDetailView.as_view(), name='detail')
]



