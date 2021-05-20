# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import requests
from dtf import dtf
from igrm import igrm
from vg import vg
from main.models import Post, Like, Dislike
from .forms import LoginForm,EnterForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

def index(request):

    #Post.objects.all().delete()
    #dtf.dtf_main()
    #igrm.igrm_main()
    #vg.vg_main()

    posts = Post.objects.filter().order_by("-pub_date")
    context = {"posts":posts}
    return render (request, "main/index.html", context)

def dtf_(request):

    site = "dtf"

    posts = Post.objects.filter(site = site).order_by("-pub_date")
    context = {"posts":posts}

    return render (request, "main/dtf.html", context)

def igrm_(request):

    site = "igromania"

    posts = Post.objects.filter(site = site).order_by("-pub_date")
    context = {"posts":posts}

    return render (request, "main/igrm.html", context)

def vg_(request):
    
    site = "vgtimes"

    posts = Post.objects.filter(site = site).order_by("-pub_date")
    context = {"posts":posts}

    return render (request, "main/vg.html", context)

def details(request, post_id):
    
    post = Post.objects.get(post_id = post_id)
    likes = Like.objects.filter(post = post).count()
    dislikes = Dislike.objects.filter(post = post).count()
    context = {'post': post, 'likes':likes, 'dislikes':dislikes}
    return render(request, 'main/details.html', context)

def register_page(request):

    _LoginForm = LoginForm()
    context = {'login_form':_LoginForm}
    return render(request, 'main/register.html', context)

def register(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(name, email, password)
        context = {'user': user}
        return redirect('//127.0.0.1:8000/accounts/login/')

def like(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(post_id = post_id)
        likes = Like.objects.filter(user = request.user, post = post_id) 

        if likes.exists() :
            link = '//127.0.0.1:8000/main/' + str(post_id)
            return redirect(link)

        else:
            like = Like(post = post, user = request.user)
            like.save()
            link = '//127.0.0.1:8000/main/' + str(post_id)
            return redirect(link)

def dislike(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(post_id = post_id)
        dislikes = Dislike.objects.filter(user = request.user, post = post_id) 

        if dislikes.exists() :
            link = '//127.0.0.1:8000/main/' + str(post_id)
            return redirect(link)

        else:
            dislike = Dislike(post = post, user = request.user)
            dislike.save()
            link = '//127.0.0.1:8000/main/' + str(post_id)
            return redirect(link)




