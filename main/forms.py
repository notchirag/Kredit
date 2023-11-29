from django import forms
from .models import Entries, Installment

class addForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control mb-2"}))
    father = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control mb-2"}))
    borrow_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={ "class": "form-control mb-2", "type":"date"}))
    contact_one = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"type":"tel", "class": "form-control mb-2"}))
    contact_two = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"type":"tel", "class": "form-control mb-2"}))
    principal = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={ "class": "form-control mb-2"}))
    interest = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={ "class": "form-control mb-2"}))
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control mb-2"}))
    guarantor = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control mb-2"}))
    contact_guar = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"type":"tel", "class": "form-control mb-2"}))
    status = forms.BooleanField(required=False, widget=forms.widgets.HiddenInput(attrs={"class": "form-control mb-2"}))
    identity = forms.FileField(required=True, widget=forms.widgets.ClearableFileInput(attrs={"class": "form-control mb-2"}))

    class Meta:
        model = Entries
        exclude = ("user", "due_date")

class dueForm(forms.ModelForm):
    due_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={ "class": "form-control mb-2", "type":"date"}))

    class Meta:
        model = Entries
        fields = ["due_date"]

class instForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control mb-2"}))
    date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={ "class": "form-control mb-2", "type":"date"}))
    amount = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={ "class": "form-control mb-2"}))

    class Meta:
        model = Installment
        exclude = ("user","entry")
