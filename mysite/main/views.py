from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
#u can also extend the above form
'''
def homepage(request):
    return HttpResponse("<h1>Awesome</h1>")

'''
def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials":Tutorial.objects.all}
                  )

def register(request):
    if request.method == 'POST':   # this is when u click submit
        form = UserCreationForm(request.POST)
        if form.is_valid(): # checks if user is exit or not and all suhc stuff
            user = form.save()
            login(request,user) # bcz u dont want to make usre login again!
            return redirect("main:homepage")# main is app name and homepage is inside that
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request,"main/register.html",context={"form":form})

