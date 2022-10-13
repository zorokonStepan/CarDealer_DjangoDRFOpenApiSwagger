from django import forms

from .models import CarBrand


class CheckBoxFalseForm(forms.Form):
    sorted_count = forms.BooleanField(required=False, initial=False, label="Сортировать по количеству")


class CheckBoxTrueForm(forms.Form):
    sorted_count = forms.BooleanField(required=False, initial=True, label="Сортировать по количеству")


class BrandsForm(forms.Form):
    # brand = forms.MultipleChoiceField(required=False, choices=CarBrand.objects.all(), label='марка авто')
    brand = forms.ModelChoiceField(queryset=CarBrand.objects.all(), initial=True,
                                   widget=forms.CheckboxSelectMultiple({'initial': True, 'required': False}),
                                   label='Марка авто')
    # brand = forms.ModelMultipleChoiceField(queryset=CarBrand.objects.all(),
    #                                        widget=forms.SelectMultiple,
    #                                        # widget=forms.CheckboxSelectMultiple,
    #                                        label='Марка авто')
    # brand = forms.MultipleChoiceField(choices=[(b.__str__, b.__str__) for b in CarBrand.objects.all()],
    #                                   widget=forms.SelectMultiple,
    #                                   # widget=forms.CheckboxSelectMultiple,
    #                                   label='Марка авто')


