from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Blogtopic, Blogentry, Blogcomment
from .forms import BlogtopicForm, BlogentryForm, BlogcommentForm



@login_required
def blogtopics(request):
    'выводит список тем'
    blogtopics = Blogtopic.objects.order_by('blogdate_added')
    context = {'blogtopics': blogtopics}
    return render(request, 'blog/blogtopics.html', context)

@login_required
def blogtopic(request, blogtopic_id):
    blogtopic = Blogtopic.objects.get(id=blogtopic_id)
    read_more = '...продолжить читать статью'
   # if topic.owner != request.user:
    #    raise Http404
    blogentries = blogtopic.blogentry_set.order_by('-blogdate_added')
    for blogentry in blogentries:
        if len(blogentry.blogtext) > 50:
            blogentry.text = blogentry.blogtext[:50]
    context = {'blogtopic': blogtopic, 'blogentries':blogentries, 'read_more':read_more}
    return render(request, 'blog/blogtopic.html', context)


@login_required
def new_blogentry(request, blogtopic_id):
    blogtopic = Blogtopic.objects.get(id=blogtopic_id)

    if request.method != 'POST':
        form = BlogentryForm()
    else:
        form = BlogentryForm(data=request.POST)
        if form.is_valid():
            new_blogentry = form.save(commit=False)
            new_blogentry.blogtopic = blogtopic
            new_blogentry.save()
            return  HttpResponseRedirect(reverse('blog:blogtopic', args=[blogtopic_id]))
    context = {'blogtopic': blogtopic, 'form': form}
    return render(request, 'blog/new_blogentry.html', context)

@login_required
def edit_blogentry(request, blogentry_id):
    blogentry = Blogentry.objects.get(id=blogentry_id)
    blogtopic = blogentry.blogtopic
    if blogtopic.blogowner != request.user:
        raise Http404

    if request.method != 'POST':
        form = BlogentryForm(instance=blogentry)
    else:
        form = BlogentryForm(instance=blogentry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:blogtopic', args=[blogtopic.id]))
    context = {'blogentry': blogentry, 'blogtopic':blogtopic, 'form': form}
    return render(request, 'blog/edit_blogentry.html', context)

def blogentry(request, blogentry_id):
    blogentry = Blogentry.objects.get(id=blogentry_id)
    blogtopic = blogentry.blogtopic
    all_comments = Blogcomment.objects.filter(blogpost=blogentry).order_by('blogcreated')
    if request.method != 'POST':
        form = BlogcommentForm()
    else:
        form = BlogcommentForm(data=request.POST)
        if form.is_valid():
            blogcomment = form.save(commit=False)
            blogcomment.blogpost = blogentry
            blogcomment.blogname = request.user
            blogcomment.save()
            return  HttpResponseRedirect(reverse('blog:blogentry', args=[blogentry_id]))

    context = {'blogentry': blogentry, 'blogtopic':blogtopic, 'form':form, 'all_comments':all_comments}
    return render(request, 'blog/blogentry.html', context)

def add_to_fav(request, blogentry_id):
    blogentry = Blogentry.objects.get(id=blogentry_id)
    if request.user not in blogentry.bloglike.all():
        blogentry.bloglike.add(request.user)
        end = ''
    else:
        end = 'Данная статья уже добавлена в избранное'
    return HttpResponseRedirect(reverse('blog:blogentry', args=[blogentry_id]))

def remove_from_fav(request, blogentry_id):
    blogentry = Blogentry.objects.get(id=blogentry_id)
    if request.user in blogentry.bloglike.all():
        blogentry.bloglike.remove(request.user)
        end = ''
    else:
        end = 'Данная статья уже удалена из избранного'
    return HttpResponseRedirect(reverse('blog:blogfavourites'))

def blogfavourites(request):
    blogfavourites = Blogentry.objects.filter(bloglike=request.user)
    read_more = '...продолжить читать статью'
    for fav in blogfavourites:
        if len(fav.blogtext) > 50:
            fav.blogtext = fav.blogtext[:50]
    context = {'blogfavourites': blogfavourites,  'read_more':read_more}
    return render(request, 'blog/blogfavourites.html', context)

def edit_blogcomment(request, blogentry_id, blogcomment_id):
    blogcomment = Blogcomment.objects.get(id=blogcomment_id)
    blogentry = blogcomment.blogpost
    #all_comments = Comment.objects.filter(post=entry)
    #for comment in all_comments:
    if blogcomment.blogname != request.user:
        raise Http404
    else:
        if request.method != 'POST':
            form = BlogcommentForm(instance=blogcomment)
        else:
            form = BlogcommentForm(instance=blogcomment, data=request.POST)
            if form.is_valid():
                blogcomment.save()
                return HttpResponseRedirect(reverse('blog:blogentry', args=[blogentry_id]))
    context = {'blogcomment': blogcomment, 'blogentry':blogentry, 'form': form}
    return render(request, 'blog/edit_blogcomment.html', context)









