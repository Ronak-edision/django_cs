from django.shortcuts import render, redirect #redirect allows use to redirect to different page
from django.http import HttpResponse
from django.contrib.auth.models import User, auth # imports user database and auth is a function
from django.contrib import messages
from .models import Feature,CustomUser
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    """#name ='Patrick'
    context={
        'name':'patrick',
        'age':23,
        'nationality':'british',

    }"""
    features=Feature.objects.all()
    return render(request, 'index.html',{'features':features})

def counter(request):
    text=request.POST['text']
    amount_of_words= len(text.split())
    return render(request,'counter.html',{'amount':amount_of_words } )

def blog(request):
    return render(request, 'html/blog.html')

def aboutus(request):
    return render(request, 'html/aboutus.html')

def product_camera(request):
    return render(request, 'html/product_camera.html')

def research(request):
    return render(request, 'html/research.html')

def product_cart(request):
    return render(request, 'html/product_cart.html')

def launch(request):
    return render(request, 'html/launch.html')

def product_camera(request):
    return render(request, 'html/product_camera.html')

def product_lens(request):
    return render(request, 'html/product_lens.html')

def product_equipment(request):
    return render(request, 'html/product_equipment.html')

def product_accessories(request):
    return render(request, 'html/product_accessories.html')

def cv_sushant(request):
    return render(request, 'html/cv_sushant.html')

def cv_nischal(request):
    return render(request, 'html/cv_nischal.html')

def cv_ronak(request):
    return render(request, 'html/cv_ronak.html')

def cv_aakarshan(request):
    return render(request, 'html/cv_aakarshan.html')

def cv_tsewang(request):
    return render(request, 'html/cv_tsewang.html')

def form2(request):
    return render(request, 'html/form2.html')

def form1(request):
    
    if request.method == 'POST':
        
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        mobile_number = request.POST['mobileNo']
        age = request.POST['age']
        gender = request.POST['gender']
        message = request.POST['message']
        email = request.POST['email']
        """ # Now, you can use these variables as needed.
        user = CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            age=age,
            gender=gender,
            message=message,
            email=email
        )
        user.save()"""

        return render(request, 'html/form1.html')
 

