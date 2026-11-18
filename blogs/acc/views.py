
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "acc/login.html", {
                "error": "username ya da parola yanlış"
            })

    return render(request, "acc/login.html")
    

def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        return redirect("login")
    return render(request, "acc/register.html")

def logout_request(request):
    logout(request)
    return redirect("index")