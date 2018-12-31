from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


@login_required
def home(request):
    return render(request, 'home.html', {'user': "ismaeel"})

@require_http_methods(["GET", "POST"])
def sign_up(request):
    """
    Signup new user
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'home.html', {'user': user})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
# @require_http_methods(["GET", "POST"])
# def sign_in(request):
#     """
#     Signin user
#     """
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return HttpResponse("Hello, Django!")
#     else:
#         form = UserCreationForm()
#     return render(request, 'home.html', {'form': form})