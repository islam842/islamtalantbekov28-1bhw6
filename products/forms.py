from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField(required=False)
    rate = forms.FloatField(required=False)


class ReviewCreateForm(forms.Form):
    title = forms.CharField()