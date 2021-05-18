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
    fresh.filler()
    posts = Post.objects.filter().order_by("-pub_date")
    context = {"posts":posts}
    return render (request, "main/index.html", context)

def dtf_(request):

    site = "dtf"
    #names = dtf.dtf_names()
    #links = dtf.dtf_links()
    #conts = dtf.dtf_content()
    #dts = dtf.dtf_date_time()
    #date = dtf.dtf_date()
    #time = dtf.dtf_time()

    #Post.objects.all().delete()
    #for i in range(0,10):
        #p = Post(site = site, title = names[i], date = date[i], time = time[i], text = conts[i])
        #p.save()
    dtf.dtf_img()
    posts = Post.objects.filter(site = site)
    context = {"posts":posts}

    return render (request, "main/dtf.html", context)

def igrm_(request):

    site = "igromania"
    igrm.igrm_img()

    #Post.objects.all().delete()
    #for i in range(0,10):
        #p = Post(site = site, title = names[i], date = date[i], time = time[i], text = conts[i])
        #p.save()

    posts = Post.objects.filter(site = site)
    context = {"posts":posts}

    return render (request, "main/igrm.html", context)

def vg_(request):
    
    site = "vgtimes"
    vg.vg_img()

    #Post.objects.all().delete()
    #for i in range(0,10):
        #p = Post(site = site, title = names[i], date = date[i], time = time[i], text = conts[i])
        #p.save()

    posts = Post.objects.filter(site = site)
    context = {"posts":posts}

    return render (request, "main/vg.html", context)

