# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from accounts.models import CustomUser
# from django.shortcuts import render, redirect
#
# from accounts.forms import LoginForm, RegisterForm
#
#
# def auth_view(request):
#     if request.method == 'POST':
#         # Login
#         if 'Login' in request.POST:
#
#             form = LoginForm(request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data.get('login_username')
#                 password = form.cleaned_data.get('login_password')
#                 remember_me = form.cleaned_data.get('remember_me')
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     if remember_me:
#                         request.session.set_expiry(60 * 60 * 24 * 30)
#                     return redirect('home')
#             else:
#                 form.add_error(None, 'Invalid username or password.')
#         # Sign_UP
#         else:
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['register_username']
#                 first_name = form.cleaned_data['register_first_name']
#                 last_name = form.cleaned_data['register_last_name']
#                 email = form.cleaned_data['register_email']
#                 password = form.cleaned_data['register_password1']
#                 policy = request.POST.get('register-policy-2')
#                 if policy == 'on':
#                     user = CustomUser.objects.create_user(username=username, email=email, password=password,
#                                                     first_name=first_name, last_name=last_name)
#                     login(request, user)
#                     return redirect('home')
#                 else:
#                     messages.error(request, 'Please accept the privacy policy to proceed.')
#
#
#     else:
#         return render(request, 'accounts/auth.html', {'login_form': LoginForm(), 'register_form': RegisterForm()})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import CustomUser
from .forms import LoginForm, RegisterForm

def auth_view(request):
    if request.method == 'POST':
        if 'Login' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('login_username')
                password = form.cleaned_data.get('login_password')
                remember_me = form.cleaned_data.get('remember_me')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    if remember_me:
                        request.session.set_expiry(60 * 60 * 24 * 30)  # 30 days
                    return redirect('home')
                else:
                    form.add_error(None, 'Invalid username or password.')
            return render(request, 'accounts/auth.html', {'login_form': form, 'register_form': RegisterForm(), 'active_tab': 'Login'})

        else:
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['register_username']
                first_name = form.cleaned_data['register_first_name']
                last_name = form.cleaned_data['register_last_name']
                email = form.cleaned_data['register_email']
                password = form.cleaned_data['register_password1']
                user = CustomUser.objects.create_user(username=username, email=email, password=password,
                                                      first_name=first_name, last_name=last_name)
                login(request, user)
                return redirect('home')

            return render(request, 'accounts/auth.html', {'login_form': LoginForm(), 'register_form': form , 'active_tab': 'Register'})

    else:
        return render(request, 'accounts/auth.html', {'login_form': LoginForm(), 'register_form': RegisterForm(), 'active_tab': 'Login' })



def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')