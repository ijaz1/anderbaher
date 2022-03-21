import email
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from admin_module.models import contactUs,category_images, employerDetails
from app1.models import get_an_estimate,signUp

# Create your views here.

def fnMaster(request):
    obj_contact_us=contactUs.objects.get(id=1)
    context={'contact_us':obj_contact_us}
    return render(request,'index_Master.html',context)

def fnIndex(request):
    obj_contact_us=contactUs.objects.get(id=1)
    context={'contact_us':obj_contact_us}
    return render(request, 'index.html',context)


def fnClient(request):
    return render(request, 'client.html')



def fnImage_Gallery(request):
    obj_image=category_images.objects.filter(category='balcony',status='available')
    print(obj_image)
    context={'photo':obj_image}
    return render(request, 'image_galery.html',context)


def fnLogIn(request):
    if request.method == 'POST':
        name = request.POST['email']
        password = request.POST['password']
        try:
            obj_client_email_check=signUp.objects.filter(email=name).exists()
            obj_employer_email_check=employerDetails.objects.filter(signIn_Email=name,status='available').exists()
            if name == 'admin@anderbaher.com' and password == 'anderbaher@123':
                request.session['admin']='111'
                return redirect('admin_panel')
            elif obj_client_email_check==True:
                obj_check_client_password=signUp.objects.get(email=name,password=password)
                request.session['client']=obj_check_client_password.id
                return redirect('client_home')
            elif obj_employer_email_check==True:
                obj_employer_password_check=employerDetails.objects.get(signIn_Email=name,signIn_Password=password)
                print('iiiiii',obj_employer_password_check)
                request.session['employer']=obj_employer_password_check.id
                return redirect('employer_home')
            else:
                messages.error(
                    request, 'Your email is wrong try again')
                return redirect('index')
        except:
            messages.error(request, 'Your password is wrong try again')
            return redirect('index')
    else:
        messages.error(request, 'Something went wrong try again')
        return redirect('index')

def fnGarden(request):
    obj_image=category_images.objects.filter(category='garden',status='available')
    print(obj_image)
    context={'photo':obj_image}
    return render(request, 'image_galery.html',context)

def fnTerrace(request):
    obj_image=category_images.objects.filter(category='terrace',status='available')
    print(obj_image)
    context={'photo':obj_image}
    return render(request, 'image_galery.html',context)

def fnPlants(request):
    obj_image=category_images.objects.filter(category='plants',status='available')
    print(obj_image)
    context={'photo':obj_image}
    return render(request, 'image_galery.html',context)

def test(request):
    return render(request,'test.html')

def fnBook_online_consultation(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        villa_apartment_property=request.POST['villa_apartment_property']
        city_zip=request.POST['city_zip']
        estimated_budget=request.POST['estimated_budget']
        when_to_start_work=request.POST['when_to_start_work']
        get_an_estimate(name=name,email=email,phone=phone,villa_apartment_property=villa_apartment_property,city_zip=city_zip,estimated_budget=estimated_budget,when_to_start_work=when_to_start_work,checkout='notchecked').save()
        messages.success(request,'YOU GET A CONFIRMATION CALL')
        return redirect('index')
    else:
        messages.success(request,'some thing went wrong')
        return redirect('index')

def fnSignUp(request):
    if request.method=='POST':
        name= request.POST['name']
        email=request.POST['email']
        obj_email_check=signUp.objects.filter(email=email).exists()
        if obj_email_check==False:
            password=request.POST['password']
            what_are_you_looking_for=request.POST['what_are_you_looking_for']
            signUp(name=name,email=email,password=password,what_are_you_looking_for=what_are_you_looking_for).save()
            messages.success(request,'YOU HAVE SUCCESSFULLY CREATED AN ANDERBAHER ACCOUNT')
            return redirect('index')
        else:
            messages.success(request,'This email is already exist')
            return redirect('index')
    else:
        messages.success(request,'some thing went wrong')
        return redirect('index')
