# Django forms ko import karo
from django import forms
# Note model ko import karo
from .models import Note


# Note create/edit karne ke liye form
class NoteForm(forms.ModelForm):
    # Rang picker field - user apna pसанध rang choose kar sake
    color = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'color', 'class': 'color-picker'}),
        initial='#FFFF99',  # Default yellow rang
    )

    class Meta:
        # Yeh form kis model ke liye hai
        model = Note
        # Kaunse fields show karane hain form mein
        fields = ['title', 'content', 'color', 'pinned']
        # HTML input widgets ki custom settings
        widgets = {
            # Title ke liye text input
            'title': forms.TextInput(attrs={
                'placeholder': 'Note title...',
                'autofocus': True,  # Jab page load ho toh title field mein focus ho
            }),
            # Content ke liye textarea (bara box)
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your note here...',
                'rows': 8,  # 8 lines ki height
            }),
        }
