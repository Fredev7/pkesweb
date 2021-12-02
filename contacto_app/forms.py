from django import forms

class ContactForm(forms.Form):

    nombre= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}), required=True)

    email= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}), required=True)
    
    contenido=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}), required=True)