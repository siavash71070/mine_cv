from django.shortcuts import render

# Create your views here.

def index_view(request):
    name = "Siavash"
    last_name = "Parhizkar"
    
    return render(request, 'index.html', {"name": name, "last_name": last_name})

def about_view(request):
    name = "Siavash"
    last_name = "Parhizkar"
    email = "Bidadparhizkar@yahoo.com"
    phone_number = "+98 9375324524"
    age = "32"
    city = "Tehran, Iran"
    degree = "Bachelor"
    
    return render(request, 'about.html',
                 {"email": email, "phone_number": phone_number,
                  "age": age, "city": city, "degree": degree, "name": name, "last_name": last_name})

def resume_view(request):
    
    return render(request, 'resume.html')