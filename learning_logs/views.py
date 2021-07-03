from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry, Comment
from .forms import TopicForm, EntryForm, CommentForm


def index(request):
    top = Entry.objects.order_by('-date_added')[:5]
    read_more = '...продолжить читать статью'
    for entry in top:
        topic = entry.topic
        id = topic.id
        if len(entry.text) > 110:
            entry.text = entry.text[:110]
    context = {'top': top, 'read_more': read_more, 'topic': topic, 'id': id}
    return render(request, 'learning_logs/index.html', context)


def topics(request):
    'выводит список тем'
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    read_more = '...продолжить читать статью'
    entries = topic.entry_set.order_by('-date_added')
    for entry in entries:
        if len(entry.text) > 50:
            entry.text = entry.text[:50]
    context = {'topic': topic, 'entries': entries, 'read_more': read_more}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    if request.user.username != 'denis':
        return render(request, 'learning_logs/foradmin.html')
    '''определяет новую тему'''
    if request.method != 'POST':
        # данные не отправлялись, создаётся пустая форма.
        form = TopicForm()
    else:
        # отправлены данные POST; обработать данные
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            # new_topic.topicimage = form.instance
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    if request.user.username != 'denis':
        return render(request, 'learning_logs/foradmin.html')
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)  # data
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    if request.user.username != 'denis':
        return render(request, 'learning_logs/foradmin.html')
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('entry', args=[entry.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    all_comments = Comment.objects.filter(active=True, post=entry).order_by('created')
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = entry
            comment.name = request.user
            comment.save()
            return HttpResponseRedirect(reverse('entry', args=[entry_id]))

    context = {'entry': entry, 'topic': topic, 'form': form, 'all_comments': all_comments, 'delete_entry': delete_entry}
    return render(request, 'learning_logs/entry.html', context)


@login_required
def delete_entry(request, topic_id, entry_id):
    entry = Entry.objects.filter(id=entry_id).delete()
    return HttpResponseRedirect(reverse('topic', args=[topic_id]))


@login_required
def add_to_fav(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if request.user not in entry.like.all():
        entry.like.add(request.user)
        end = ''
    else:
        end = 'Данная статья уже добавлена в избранное'
    return HttpResponseRedirect(reverse('entry', args=[entry_id]))


@login_required
def remove_from_fav(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if request.user in entry.like.all():
        entry.like.remove(request.user)
        end = ''
    else:
        end = 'Данная статья уже удалена из избранного'
    return HttpResponseRedirect(reverse('favourites'))


@login_required
def favourites(request):
    favourites = Entry.objects.filter(like=request.user)
    read_more = '...продолжить читать статью'
    for fav in favourites:
        if len(fav.text) > 50:
            fav.text = fav.text[:50]
    context = {'favourites': favourites, 'read_more': read_more}
    return render(request, 'learning_logs/favourites.html', context)


@login_required
def edit_comment(request, entry_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    entry = comment.post
    # all_comments = Comment.objects.filter(post=entry)
    # for comment in all_comments:
    if comment.name != request.user:
        raise Http404
    else:
        if request.method != 'POST':
            form = CommentForm(instance=comment)
        else:
            form = CommentForm(instance=comment, data=request.POST)
            if form.is_valid():
                comment.save()
                return HttpResponseRedirect(reverse('entry', args=[entry_id]))
    context = {'comment': comment, 'entry': entry, 'form': form}
    return render(request, 'learning_logs/edit_comment.html', context)
