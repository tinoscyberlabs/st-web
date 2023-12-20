from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Event_Details_Model,Event_Registration,MinistriesModel,Daily_Mass,Special_Masses,Obituary_Model,Gallery_Model,Blog_Model,Blog_News_Model
from .forms import Event_Details_Form,Event_Registration_form,MinistriesForm,Daily_Mass_Form,Special_Masses_Form,Obituary_Form,Gallery_Form,Blog_Form,Blog_News_Form
from django.shortcuts import get_object_or_404
from datetime import date
from django.utils import timezone
import os
# Create your views here.

def index(request):
    active_events = Event_Details_Model.objects.filter(end_date__gte=timezone.now())
    events = Event_Details_Model.objects.all()
    ministries = MinistriesModel.objects.all()
    gallery = Gallery_Model.objects.all()
    blog = Blog_Model.objects.all()
    return render(request,'index.html',{'active_events':active_events,'events':events,'ministries':ministries,'gallery':gallery,'blog':blog})

def about(request):
    return render(request,'about-us.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.success(request, ("There Was An Error Loging In, Try Again..."))
            return redirect('login')
    return render(request,'authenticate/login.html')

def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request,'admin-dashboard.html')
    else:
        return redirect('login_user')

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')

def bishop_message(request):
    return render(request,'bishop-message.html')

def vicar_message(request):
    return render(request,'vicar-message.html')

def image_shadow(request):
    return render(request,'image-shadow.html')

def january(request):
    return render(request,'january.html')

def admin_add_events(request):
    if request.method == 'POST':
        form = Event_Details_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('admin_event_view')  # Redirect to a page showing all products
    else:
        form = Event_Details_Form()

    return render(request, 'admin_add_events.html', {'form': form})

def admin_event_view(request):
    events = Event_Details_Model.objects.all()
    return render(request,'admin_event_view.html',{'events':events})


def admin_update_events(request, id):
    events = get_object_or_404(Event_Details_Model, id=id)

    if request.method == 'POST':
        form = Event_Details_Form(request.POST, instance=events)
        if form.is_valid():
            form.save()
            return redirect('admin_event_view')
    else:
        form = Event_Details_Form(instance=events)

    return render(request, 'admin_update_events.html', {'form': form, 'events':events})

def admin_delete_events(request,id):
    events = Event_Details_Model.objects.get(id=id)
    events.delete()
    return redirect('admin_event_view')

def Event_Details(request,id):
    events = Event_Details_Model.objects.get(id=id)
    return render(request,'event-details.html',{'events':events,'id':id})


def event_registration(request):
    event_name = Event_Details_Model.objects.filter(event_name=event_name)
    if request.method == 'POST':
        name = request.POST.get['name']
        email = request.POST.get['email']
        phone = request.POST.get['phone']
        data = Event_Registration(name=name,email=email,phone=phone)
        data.save()
        return HttpResponse('data added successfully')
    return render(request,'event-details.html',{'event_name':event_name})

def admin_add_ministries(request):
    if request.method == 'POST':
        ministries = MinistriesForm(request.POST, request.FILES)
        if ministries.is_valid():
            ministries.save()
            return HttpResponseRedirect('admin_ministries_view')  # Redirect to a page showing all products
    else:
        ministries = MinistriesForm()

    return render(request, 'admin_add_ministries.html', {'ministries': ministries})

def admin_ministries_view(request):
    view = MinistriesModel.objects.all()
    return render(request, 'admin_ministries_view.html', {'view': view})

def admin_update_ministries(request, id):
    ministries = get_object_or_404(MinistriesModel, id=id)

    if request.method == 'POST':
        form = MinistriesForm(request.POST, instance=ministries)
        if form.is_valid():
            form.save()
            return redirect('admin_ministries_view')
    else:
        form = MinistriesForm(instance=ministries)

    return render(request, 'admin_update_ministries.html', {'form': form, 'ministries':ministries})

def admin_delete_ministries(request,id):
    ministries = MinistriesModel.objects.get(id=id)
    ministries.delete()
    return redirect('admin_ministries_view')

def admin_add_mass_times(request):
    if request.method == 'POST':
        mass_days = request.POST['mass_days']
        mass_date = request.POST['mass_date']
        mass_time = request.POST['mass_time']
        end_time = request.POST['end_time']
        mass_description = request.POST['mass_description']
        data = Daily_Mass(mass_days=mass_days,mass_date=mass_date,mass_time=mass_time,end_time=end_time,mass_description=mass_description)
        data.save()
        return HttpResponseRedirect('admin_daily_mass_view')
    return render(request,'admin_add_mass_times.html')

def admin_daily_mass_view(request):
    mass_times = Daily_Mass.objects.all()
    return render(request,'admin_daily_mass_view.html',{'mass_times':mass_times})


def admin_update_mass_times(request,id):
    data=Daily_Mass.objects.get(id=id)
    mass=Daily_Mass_Form(instance=data)
    if request.method=='POST':
        mass=Daily_Mass_Form(request.POST,request.FILES,instance=data)
        if mass.is_valid():
            mass.save()
            return redirect('admin_daily_mass_view')
    return render(request,'admin_update_mass_times.html',{'mass':mass})

def admin_delete_mass_times(request,id):
    mass_times = Daily_Mass.objects.get(id=id)
    mass_times.delete()
    return redirect('admin_daily_mass_view')

def admin_add_special_masses(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        date = request.POST['date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        description = request.POST['description']
        data = Special_Masses(event_name=event_name,date=date,start_time=start_time,end_time=end_time,description=description)
        data.save()
        return HttpResponseRedirect('admin_special_mass_view')
    return render(request,'admin_add_special_masses.html')

def admin_special_mass_view(request):
    special_mass = Special_Masses.objects.all()
    return render(request,'admin_special_mass_view.html',{'special_mass':special_mass})

def admin_update_special_mass(request,id):
    data=Special_Masses.objects.get(id=id)
    special_mass=Special_Masses_Form(instance=data)
    if request.method=='POST':
        special_mass=Special_Masses_Form(request.POST,request.FILES,instance=data)
        if special_mass.is_valid():
            special_mass.save()
            return redirect('admin_special_mass_view')
    return render(request,'admin_update_special_mass.html',{'special_mass':special_mass})

def admin_delete_special_mass(request,id):
    special_mass = Special_Masses.objects.get(id=id)
    special_mass.delete()
    return redirect('admin_special_mass_view')
def mass_times(request):
    daily_mass = Daily_Mass.objects.all()
    special_mass = Special_Masses.objects.all()
    return render(request,'masses.html',{'daily_mass':daily_mass,'special_mass':special_mass})

def obituary(request):
    obituary = Obituary_Model.objects.all()
    return render(request,'obituary.html',{'obituary':obituary})

def admin_add_obituary(request):
    if request.method == 'POST':
        obituary = Obituary_Form(request.POST, request.FILES)
        if obituary.is_valid():
            obituary.save()
            return HttpResponseRedirect('admin_obituary_view')  # Redirect to a page showing all products
    else:
        obituary = Obituary_Form()

    return render(request, 'admin_add_obituary.html', {'obituary': obituary})

def admin_obituary_view(request):
    obituary = Obituary_Model.objects.all()
    return render(request,'admin_obituary_view.html',{'obituary':obituary})

def admin_update_obituary(request,id):
    data=Obituary_Model.objects.get(id=id)
    obituary=Obituary_Form(instance=data)
    if request.method=='POST':
        obituary=Obituary_Form(request.POST,request.FILES,instance=data)
        if obituary.is_valid():
            obituary.save()
            return redirect('admin_obituary_view')
    return render(request,'admin_update_obituary.html',{'obituary':obituary})

def admin_delete_obituary(request,id):
    obituary = Obituary_Model.objects.get(id=id)
    obituary.delete()
    return redirect('admin_obituary_view')

def gallery(request):
    gallery = Gallery_Model.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})

def admin_add_gallery(request):
    if request.method == 'POST':
        gallery = Gallery_Form(request.POST, request.FILES)
        if gallery.is_valid():
            gallery.save()
            return HttpResponseRedirect('admin_gallery_view')  # Redirect to a page showing all products
    else:
        gallery = Gallery_Form()

    return render(request, 'admin_add_gallery.html', {'gallery': gallery})

def admin_gallery_view(request):
    gallery = Gallery_Model.objects.all()
    return render(request,'admin_gallery_view.html',{'gallery':gallery})

def admin_update_gallery(request,id):
    data = Gallery_Model.objects.get(id=id)
    gallery = Gallery_Form(instance=data)
    if request.method == 'POST':
        gallery = Gallery_Form(request.POST,request.FILES,instance=data)
        if gallery.is_valid():
            gallery.save()
            return redirect('admin_gallery_view')
    return render(request,'admin_update_gallery.html',{'gallery':gallery})

def admin_delete_gallery(request,id):
    gallery = Gallery_Model.objects.get(id=id)
    gallery.delete()
    return redirect('admin_gallery_view')

def admin_add_blog(request):
    if request.method == 'POST':
        blog = Blog_News_Form(request.POST, request.FILES)
        if blog.is_valid():
            blog.save()
            return HttpResponseRedirect('admin_blog_view')  # Redirect to a page showing all products
    else:
        blog = Blog_News_Form()

    return render(request, 'admin_add_blog.html', {'blog': blog})

def admin_blog_view(request):
    blog = Blog_News_Model.objects.all()
    return render(request,'admin_blog_view.html',{'blog':blog})

def admin_update_blog(request,id):
    data = Blog_News_Model.objects.get(id=id)
    blog = Blog_News_Form(instance=data)
    if request.method == 'POST':
        blog = Blog_News_Form(request.POST,request.FILES,instance=data)
        if blog.is_valid():
            blog.save()
            return redirect('admin_blog_view')
    return render(request,'admin_update_blog.html',{'blog':blog})

def admin_delete_blog(request,id):
    blog = Blog_News_Model.objects.get(id=id)
    blog.delete()
    return redirect('admin_blog_view')

def blog_single(request):
    return render(request,'blog-single.html')