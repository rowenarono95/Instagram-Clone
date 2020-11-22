from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from .models import Post, Profile
from .forms import NewPostForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
def home(request):
    images = Post.objects.all()
    return render(request, 'index.html', {"images": images})
    

@login_required(login_url="/accounts/login/")
def new_post(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = current_user
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
            post = Post(image = image,caption = caption,profile = user_profile)
            post.save_post()
            # post.save()
        return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})


def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('index')

    else:
        
        profile_form = ProfileUpdateForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        context = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'profile.html', context)

    