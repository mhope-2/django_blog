from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from blog.models import Post
from blog.forms import CreateBlogForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
import datetime



# Create your views here.

class IndexView(TemplateView):
    template_name = "blog/index.html"
    model = Post
    success_url = ''

    def get(self, request, *args, **kwargs):

        current_year = datetime.datetime.now().year

        post_queryset = reversed(Post.objects.all())
        
        return render(request, self.template_name, {'post_queryset':post_queryset, 'current_year':current_year})




# create new blog
class CreateBlogView(LoginRequiredMixin, CreateView):
    template_name = "blog/create.html"
    login_url = '/user/login/'
    redirect_field_name = 'next'
    # success_url = '/blog/create/'
    # form_class = CreateBlogForm
    # form = {'form':form_class}
    model = Post

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):

        if request.POST['author']:

            if User.objects.filter(username=str(request.POST['author'])).exists():

                post_instance = Post(author_id=request.user.id, title=request.POST['title'], body=request.POST['body'])
                post_instance.save()

                return redirect('/')
            else:
                return render(request, 'blog/create.html', {'unauth_author':'Unauthorized Author'})
        
        return render(request, self.template_name)



# Create your views here.

class PostDetailView(TemplateView):
    template_name = "blog/detail.html"
    model = Post
    success_url = ''

    def get(self, request, id, *args, **kwargs):

        try:

            post_detail_queryset = Post.objects.get(id=id)

        except Exception as e:
            
            #ideal: log exception

            #temp
            post_detail_queryset = Post.objects.get(id=id)


        current_year = datetime.datetime.now().year
        
        return render(request, self.template_name, {'post_detail_queryset':post_detail_queryset, 'current_year':current_year})
        