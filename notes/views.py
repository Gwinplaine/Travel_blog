from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Notesentry
from .forms import NotesentryForm

@login_required
def notes(request):
    'выводит список тем'
    notes = Notesentry.objects.filter(notesowner=request.user).order_by('notesdate_added')
    read_more = '...продолжить читать заметку'
    for note in notes:
        if note.notesowner != request.user:
            raise Http404
        if len(note.notestext) > 50:
            note.notestext = note.notestext[:50]

    context = {'notes':notes, 'read_more':read_more}
    return render(request, 'notes/notes.html', context)

@login_required
def note(request, note_id):
    note = Notesentry.objects.get(id=note_id)
    if note.notesowner != request.user:
        raise Http404
    context = {'note': note}
    return render(request, 'notes/note.html', context)


@login_required
def new_note(request):
    notes = Notesentry.objects.filter(notesowner=request.user).order_by('notesdate_added')
    #if note.notesowner != request.user:
     #   raise Http404
    if request.method != 'POST':
        #данные не отправлялись, создаётся пустая форма.
        form = NotesentryForm()
    else:
        #отправлены данные POST; обработать данные
        form = NotesentryForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.notesowner = request.user
            new_note.save()
            return HttpResponseRedirect(reverse('notes:notes'))
    context = {'form': form}
    return render(request, 'notes/new_note.html', context)

@login_required
def edit_note(request, note_id):
    note = Notesentry.objects.get(id=note_id)
    if note.notesowner != request.user:
        raise Http404
    if request.method != 'POST':
        form = NotesentryForm(instance=note)
    else:
        form = NotesentryForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notes:note', args=[note.id]))
    context = {'note': note, 'form': form}
    return render(request, 'notes/edit_note.html', context)











