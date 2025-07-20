from django import forms
from .models import Blog, Tag

class BlogForm(forms.ModelForm): # used to create a form
    class Meta: # used to configure the form
        model = Blog # model to create the form for
        fields = [ # fields to include in the form
            'title',
            'pub_date',
            'image',
            'draft',
            'blog_type',
            'description',
            'tags',
        ]
        exclude = ['author'] # Prevent users from editing/deleting other users' blogs (on the backend), but allow them to edit their own
        widgets = { # used to configure the form fields
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'tags': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'rows': 5}),
        }
