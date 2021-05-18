from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import bs4, requests
import re
from dtf import dtf
from igrm import igrm
from vg import vg
from main.models import Post
from fresh import fresh

def index(request):

    Post.objects.all().delete()
    dtf.dtf_main()
    igrm.igrm_main()
    vg.vg_main()

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
    context = {'post': post}
    return render(request, 'main/details.html', context)

