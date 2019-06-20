from django import forms
class Dataform(forms.Form):
    # TODO: Define form fields here
    file = forms.FileField()

