from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("status", "created_on", "updated_on")

        widgets = {
            "task_title": forms.TextInput(attrs={"class": "form-control"}),
            "project_name": forms.TextInput(attrs={"class": "form-control"}),
            "deadline": forms.DateInput(attrs={"type":"date", "class": "form-control"}),   
            "task_description": forms.Textarea(attrs={"class": "form-control content, requiredField"}),
            "author": forms.HiddenInput(),
            "status": forms.HiddenInput(),
        }




