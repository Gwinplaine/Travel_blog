from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Notesentry
from .forms import NotesentryForm


# функция представления всех заметок на странице
@login_required
def notes(request):
    notes = Notesentry.objects.filter(notesowner=request.user).order_by('-notesdate_added')
    read_more = '...продолжить читать заметку'
    for note in notes:
        if note.notesowner != request.user:
            return render(request, 'learning_logs/notyours.html')
        if len(note.notestext) > 50:
            note.notestext = note.notestext[:50]

    context = {'notes': notes, 'read_more': read_more}
    return render(request, 'notes/notes.html', context)


# функция представления заметки
@login_required
def note(request, note_id):
    note = Notesentry.objects.get(id=note_id)
    if note.notesowner != request.user:
        return render(request, 'learning_logs/notyours.html')
    context = {'note': note}
    return render(request, 'notes/note.html', context)


# функция добавления новой заметки
@login_required
def new_note(request):
    if request.method != 'POST':
        form = NotesentryForm()
    else:
        form = NotesentryForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.notesowner = request.user
            new_note.save()
            return HttpResponseRedirect(reverse('notes:notes'))
    context = {'form': form}
    return render(request, 'notes/new_note.html', context)


# функция изменения заметки
@login_required
def edit_note(request, note_id):
    note = Notesentry.objects.get(id=note_id)
    if note.notesowner != request.user:
        return render(request, 'learning_logs/notyours.html')
    if request.method != 'POST':
        form = NotesentryForm(instance=note)
    else:
        form = NotesentryForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notes:note', args=[note.id]))
    context = {'note': note, 'form': form}
    return render(request, 'notes/edit_note.html', context)

# функция удаления заметки
@login_required
def delete_note(request, note_id):
    note = Notesentry.objects.get(id=note_id)
    if note.notesowner != request.user:
        return render(request, 'learning_logs/notyours.html')
    else:
        note = Notesentry.objects.filter(id=note_id)
        note.delete()
    return HttpResponseRedirect(reverse('notes:notes'))
