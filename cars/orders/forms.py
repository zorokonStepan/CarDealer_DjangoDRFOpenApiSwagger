from django import forms

from .models import CarBrand


class CheckBoxForm(forms.Form):
    sorted_count = forms.BooleanField(required=False, initial=False, label="Сортировать по количеству")


class BrandsForm(forms.Form):
    brand = forms.ModelMultipleChoiceField(queryset=CarBrand.objects.all(),
                                           initial=[i for i in CarBrand.objects.all()],
                                           widget=forms.CheckboxSelectMultiple,
                                           required=False,
                                           label='Марка авто')


