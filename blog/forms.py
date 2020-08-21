from django import forms

from .models import Post, Comment,info,education,work,skills,voluneering

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class InfoForm(forms.ModelForm):

    class Meta:
        model = info
        fields = ('text',)

class educationForm(forms.ModelForm):

    class Meta:
        model = education
        fields = ('text',)

class workForm(forms.ModelForm):

    class Meta:
        model = work
        fields = ('text',)

class skillsForm(forms.ModelForm):

    class Meta:
        model = skills
        fields = ('text',)

class voluneeringForm(forms.ModelForm):

    class Meta:
        model = voluneering
        fields = ('text',)


