from django import forms


class ImageUploadForm(forms.Form):
    name = forms.TextInput()
    image = forms.ImageField()
