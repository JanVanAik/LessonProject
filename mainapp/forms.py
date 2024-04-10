from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from mainapp.models import BaseUser, Product, Order


class OrderForm(forms.ModelForm):
    order_datetime = forms.DateTimeField(widget=forms.DateTimeInput)

    class Meta:
        model = Order
        fields = ('order_datetime', 'user_id', 'product_id', 'total_price')


class ProductForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = Product
        fields = ('image', )