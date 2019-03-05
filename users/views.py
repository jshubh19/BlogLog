from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.


def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            # below code will save new user  as profile by creating it
            Profile.objects.create(user=user)
            username=form.cleaned_data.get('username')
            messages.success(request,'user {} register successfully'.format(username))
            return redirect('users:login')
    else:
        form=UserRegisterForm()
    return render(request,'signup.html',{'form':form})

@login_required(login_url='users:login')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='users:login')
def edit_profile(request):
    if request.method=="POST":
        form=EditProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()

            return redirect('users:profile')


    else:
        form=EditProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html',{'form':form})