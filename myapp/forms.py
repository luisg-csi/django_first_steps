from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Title', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label='Task description',widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProyect(forms.Form):
    name = forms.CharField(label='Name of proyect', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    
