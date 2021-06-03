from django.shortcuts import redirect, render, get_object_or_404
from .models import Signup
from django.utils import timezone
# Create your views here.

def home(request):
    signups = Signup.objects.all()
    return render(request, "home.html", {'signups':signups})

def detail(request, id):
    signup = get_object_or_404(Signup, pk=id)
    return render(request,'detail.html',{'signup':signup})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_signup = Signup()
    new_signup.name = request.POST['name']
    new_signup.age = request.POST['age']
    new_signup.pubdate = timezone.now()
    new_signup.email = request.POST['email']
    new_signup.introduce = request.POST['introduce']
    new_signup.save()
    return redirect('detail', str(new_signup.id))

def edit(request, id):
    edit_signup = get_object_or_404(Signup, pk=id)
    return render(request,'edit.html', {'signup':edit_signup})

def update(request, id):
    update_signup = get_object_or_404(Signup, pk=id)
    update_signup.age = request.POST['age']
    update_signup.writer = request.POST['writer']
    update_signup.pubdate = timezone.now()
    update_signup.email = request.POST['email']
    update_signup.introduce = request.POST['introduce']
    update_signup.save()
    return redirect('detail', str(update_signup.id))

def delete(request, id):
    delete_signup = get_object_or_404(Signup, pk=id)
    delete_signup.delete()
    return redirect('home')
