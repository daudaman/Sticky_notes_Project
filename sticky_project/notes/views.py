# Zaruri imports
from django.shortcuts import render, redirect, get_object_or_404
# Login check ke liye decorator
from django.contrib.auth.decorators import login_required
# User registration form
from django.contrib.auth.forms import UserCreationForm
# User ko login karne ke liye
from django.contrib.auth import login
# Search ke liye query operators
from django.db.models import Q
# Model aur Form ko import karo
from .models import Note
from .forms import NoteForm


# Login zaroori hai in sab functions mein
@login_required
def note_list(request):
    """
    Sab notes ko display karo, user apne search bhi kar sakta hai
    """
    # Search query ko get karo agar user ne search kia
    query = request.GET.get('q', '')
    # Sirf logged in user ke notes lao
    notes = Note.objects.filter(owner=request.user)
    # Agar search query hai toh title ya content mein dhundo
    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'notes/note_list.html', {'notes': notes, 'query': query})


@login_required
def note_create(request):
    """
    Naya note create karo
    """
    # Agar POST request hai (form submit hua)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        # Form valid hai ya nahi check karo
        if form.is_valid():
            # Form save karo lekin abhi database mein na jao
            note = form.save(commit=False)
            # Current user ko owner banao
            note.owner = request.user
            # Ab database mein save karo
            note.save()
            # Notes list page par wapas jao
            return redirect('note_list')
    # Agar GET request hai (pehle baar page open hua)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'action': 'Create'})


@login_required
def note_edit(request, pk):
    """
    Pehle se mौजood note ko edit karo
    pk = note ki ID
    """
    # Note ko get karo, agar nahi mila ya owner different hai toh 404 error do
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    # Agar POST request hai (form submit hua)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        # Form valid hai toh save karo
        if form.is_valid():
            form.save()
            # Notes list page par wapas jao
            return redirect('note_list')
    # Agar GET request hai (pehli baar page khola)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'action': 'Edit', 'note': note})


@login_required
def note_delete(request, pk):
    """
    Note ko delete karo
    pk = note ki ID
    """
    # Note ko get karo, agar nahi mila ya owner different hai toh 404 error do
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    # Agar POST request hai (user ne confirm kiya)
    if request.method == 'POST':
        # Note ko database se hatao
        note.delete()
        # Notes list page par wapas jao
        return redirect('note_list')
    # Confirm delete page show karo
    return render(request, 'notes/note_confirm_delete.html', {'note': note})


def register_view(request):
    """
    Nya user account banana (Registration)
    """
    # Agar user pehle se login hai toh notes list par bhej do
    if request.user.is_authenticated:
        return redirect('note_list')
    # Agar POST request hai (form submit hua)
    if request.method == 'POST':
        # Registration form create karo
        form = UserCreationForm(request.POST)
        # Form valid hai ya nahi check karo
        if form.is_valid():
            # Naya user create karo
            user = form.save()
            # User ko login karo (taake registration ke baad login na karna pade)
            login(request, user)
            # Notes list page par bhej do
            return redirect('note_list')
    # Agar GET request hai (pehli baar page khola)
    else:
        form = UserCreationForm()
    return render(request, 'notes/register.html', {'form': form})
