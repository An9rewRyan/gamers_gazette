# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import requests
from dtf import dtf
from igrm import igrm
from vg import vg
from main.models import Post, Like, Dislike, Comment, CommentChild, View
from .forms import LoginForm,EnterForm, CommentForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import datetime

def index(request):

    #Post.objects.all().delete()
    #dtf.dtf_main()
    #vg.vg_main()
    #igrm.igrm_main()
    likes = Like.objects.filter()
    dislikes = Dislike.objects.filter()
    views = View.objects.filter()
    posts = Post.objects.filter().order_by("-pub_date")
    context = {"posts":posts,'likes':likes, 'dislikes':dislikes, 'views':views}

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
    comments = Comment.objects.filter(post = post, display = True)
    anscomments = CommentChild.objects.filter(post = post)

    if not request.user.is_authenticated:
        pass

    else:
        views = View.objects.filter(user = request.user, post = post_id) 

        if views.exists() :
            pass

        else:
            view = View(post = post, user = request.user)
            view.save()
            post.views = post.views + 1
            post.save()

    views = View.objects.filter(post = post_id).count()

    context = {'post': post, 'likes':likes, 'dislikes':dislikes, 'comments':comments, 'anscomments':anscomments, 'views':views}

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

    post = Post.objects.filter(post_id = post_id)
    if not request.user.is_authenticated:
        link = '//127.0.0.1:8000/main/' + str(post_id)
        return redirect(link)
    else:
        if request.method == "POST":
            post = Post.objects.get(post_id = post_id)
            likes = Like.objects.filter(user = request.user, post = post_id) 

            if likes.exists() :
                link = '//127.0.0.1:8000/main/' + str(post_id)

                return redirect(link)

            else:
                like = Like(post = post, user = request.user)
                like.save()
                post.likes = post.likes+1
                post.save()
                link = '//127.0.0.1:8000/main/' + str(post_id)

                return redirect(link)

def dislike(request, post_id):

    if not request.user.is_authenticated:
        link = '//127.0.0.1:8000/main/' + str(post_id)
        return redirect(link)
    else:
        if request.method == "POST":
            post = Post.objects.get(post_id = post_id)
            dislikes = Dislike.objects.filter(user = request.user, post = post_id) 

            if dislikes.exists() :
                link = '//127.0.0.1:8000/main/' + str(post_id)
                return redirect(link)

            else:
                dislike = Dislike(post = post, user = request.user)
                dislike.save()
                post.dislikes = post.dislikes + 1
                post.save()
                link = '//127.0.0.1:8000/main/' + str(post_id)
                return redirect(link)

@login_required
def comment(request, post_id):

    _CommentForm = CommentForm()

    return render(request, 'main/comment.html',{'form':_CommentForm})

@login_required
def commenting(request, post_id):

    if request.method == "POST":
        now = datetime.datetime.now()
        text = request.POST.get("text")
        post = Post.objects.get(post_id= post_id)
        comment = Comment(texts = text,post = post, user = request.user, pub_date = now)
        comment.save()
        post.comments = post.comments + 1
        post.save()
        link = '//127.0.0.1:8000/main/' + str(post_id)

        return redirect(link)

@login_required
def anscomment(request, post_id,comment_id):

    _CommentForm = CommentForm()

    return render(request, 'main/anscomment.html',{'form':_CommentForm})

@login_required
def answering(request, post_id,comment_id):

    if request.method == "POST":
        
        now = datetime.datetime.now()
        text = request.POST.get("text")
        post = Post.objects.get(post_id = post_id)

        comment1 = Comment(texts = text,post = post, user = request.user, pub_date = now, display = False)
        comment1.save()
        comment2 = Comment.objects.get(texts = text,post = post, user = request.user, pub_date = now)

        #comment2 = Comment.objects.get(comment_id=id)
        #child = CommentChild(texts = text, copy =comment2, user = request.user, prev = comment, comment = comment, post = post)
        #child.save()
        link = '//127.0.0.1:8000/main/' + str(post_id)+'/'+str(comment_id)+'/'+str(comment2.comment_id )+'/'

        return redirect(link)

@login_required
def childing(request, post_id,comment_id, parent_id):

    comment = Comment.objects.get(comment_id=comment_id)
    parent = Comment.objects.get(comment_id = parent_id)
    text = parent.texts
    post = Post.objects.get(post_id = post_id)
    child = CommentChild(texts = text, user = request.user, prev = comment, comment = comment, post = post)
    child.save()
    post.comments = post.comments + 1
    post.save()

    link = '//127.0.0.1:8000/main/' + str(post_id)

    return redirect(link)



@login_required
def answer_child(request,post_id,comment_id,child_id):

    _CommentForm = CommentForm()

    return render(request, 'main/anschild.html',{'form':_CommentForm})

@login_required
def answering_child(request, post_id,comment_id, child_id):
    
    if request.method == "POST":

        text = request.POST.get("text")
        now = datetime.datetime.now()
        child = CommentChild.objects.get(child_id = child_id)
        post = Post.objects.get(post_id = post_id)
        copy_comment = Comment(texts = text, user = child.user , post = post, pub_date = now, display = False)
        copy_comment.save()
        comment2 = Comment.objects.get(texts = text, post = post, user = child.user, pub_date = now)
        #anscomment = CommentChild(texts = text, prev = prev, copy = copy_comment, user = request.user, comment = comment, post = post)
        #anscomment.save()
        link = '//127.0.0.1:8000/main/' + str(post_id)+'/'+str(comment_id)+'/'+str(child_id)+'/'+str(comment2.comment_id)+'/'+'really_child_answering/'

        return redirect(link)

def really_answering(request, post_id,comment_id, child_id, parent_id):

    parent = Comment.objects.get(comment_id = parent_id)
    comment = Comment.objects.get(comment_id = comment_id)
    text = parent.texts
    post = Post.objects.get(post_id = post_id)
    child = CommentChild(texts = text, prev = parent, user = request.user, comment = comment, post = post)
    child.save()
    post.comments = post.comments + 1
    post.save()

    link = '//127.0.0.1:8000/main/' + str(post_id)

    return redirect(link)
    


