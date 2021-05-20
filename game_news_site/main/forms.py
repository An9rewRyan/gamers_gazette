from django import forms

class LoginForm(forms.Form): 
    name = forms.CharField(max_length=100)
    birth_date = forms.DateField()
    password = forms.IntegerField()
    email = forms.EmailField()

class EnterForm(forms.Form): 
    name = forms.CharField(max_length=100)
    password = forms.IntegerField()

class CommentForm(forms.Form):
    text = forms.CharField(max_length=400)