
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User

def login_request(request):
    if request.user.is_authenticated:
        redirect("home")
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
    if request.user.is_authenticated:
        redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("firstname")  
        last_name = request.POST.get("lastname")   
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password or len(password) < 8 or not any(char.isdigit() for char in password):
            return render(request, "acc/register.html", {
                "error": "Parolalar eşleşmiyor ya da şifre kuralları karşılanmıyor. Lütfen tekrar deneyin."
            })

        if User.objects.filter(username=username).exists():
            return render(request, "acc/register.html", {
                "error": "Bu kullanıcı adı zaten alınmış. Lütfen başka bir kullanıcı adı deneyin."
            })

        if User.objects.filter(email=email).exists():
            return render(request, "acc/register.html", {
                "error": "Bu e-posta zaten kayıtlı. Lütfen başka bir e-posta deneyin."
            })

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        
        login(request, user)
        return redirect("index")  # Ana sayfa URL adınız neyse onu yazın (ör. "home" veya "index")

    return render(request, "acc/register.html")
def logout_request(request):
    logout(request)
    return redirect("index")