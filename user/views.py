from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
import re

# Create your views here.
class SignUpView(CreateView):
    model = get_user_model()
    # form_class = UserCreationForm
    # success_url = reverse_lazy('user_app:login')
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {'form':self.form_class})
    

    def post(self, request, *args, **kwargs):

        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']


        if User.objects.filter(username=username).exists():
            return render(request, "registration/signup.html", 
                                    {'username_exists':'User with this username already exists'}) 

        if User.objects.filter(email=email).exists():
            return render(request, "registration/signup.html", 
                                    {'email_exists':'User with this email already exists'}) 
        
        if password and password2 and password != password2:
            return render(request, "registration/signup.html", 
                                    {'password_mismatch':'Passwords do not match!'})

        if len(password) < 6:
            return render(request, "registration/signup.html", 
                                    {'invalid_length':'Password should not be less than 6 characters!'})

        # if not re.findall('[A-Z]', password):
        #     return render(request, "registration/signup.html", 
        #                             {'no_upper_case':'Password should contain at least one Uppercase'})

        # if not re.findall('\d', password):
        #     return render(request, "registration/signup.html", 
        #                             {'contain_number':'Passwords should not be less than 6 characters!'})

        if not first_name.isalpha():
            return render(request, "registration/signup.html", 
                                    {'fname_first_char_digit':'Unacceptable first name'})

        if not last_name.isalpha():
            return render(request, "registration/signup.html", 
                                    {'lname_first_char_digit':'Unacceptable last name'})                                                      

        user = User.objects.create_user(username=username, email=email, first_name=first_name, 
                                        last_name=last_name, password=password)

        login(request, user)  

        return render(request, self.template_name)



class LoginView(CreateView):

    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):

        # login contol logic
        if request.POST['username']:

            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

            if user is not None:
                # log user in
                login(request, user)
                return redirect('/blog/create')
            else:
                # No backend authenticated the credentials
                return render(request, "login/login.html", {'error_message':'Invalid Credentials'})
                            
        return render(request, self.template_name)
