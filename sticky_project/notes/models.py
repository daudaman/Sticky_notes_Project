# Django models aur User model ko import karo
from django.db import models
from django.contrib.auth.models import User


# Note ka model jo sticky notes ko represent karta hai
class Note(models.Model):
    # Note ka title
    title = models.CharField(max_length=200)
    
    # Note ki content/matelab
    content = models.TextField()
    
    # Note ka rang (hex color code mein)
    color = models.CharField(max_length=7, default='#FFFF99')
    
    # Jab note create hua tha
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Jab note ko akhri baar update kiya gaya
    updated_at = models.DateTimeField(auto_now=True)
    
    # Note ka owner (kon sa user likha hai)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    
    # Note pinned hai ya nahi (aham notes upar aayein)
    pinned = models.BooleanField(default=False)

    class Meta:
        # Pehle pinned notes, phir update ke hisaab se sort karo
        ordering = ['-pinned', '-updated_at']

    def __str__(self):
        # Note ka title display karo
        return self.title
