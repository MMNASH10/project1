from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth import login as auth_login, authenticate



def signup(request):
    template_data = {}
    template_data["title"] = "Sign Up"
    if request.method == "GET":
        template_data["form"] = CustomUserCreationForm()
        return render(request, "accounts/signup.html", {"template_data": template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.index')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})
