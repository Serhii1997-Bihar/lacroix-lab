from django import forms
from cart.models import OrderModel, ClientData

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 4)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Кількість'
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
    size = forms.ChoiceField(
        choices=[],
        required=False,
        label='Розмір'
    )

    def __init__(self, *args, **kwargs):
        sizes = kwargs.pop('sizes', None)
        super().__init__(*args, **kwargs)
        if sizes:
            self.fields['size'].choices = [(size.id, size.size) for size in sizes]
            self.fields['size'].required = True
        else:
            self.fields['size'].widget = forms.HiddenInput()


class OrderForm(forms.ModelForm):
    class Meta:
        model = ClientData
        fields = ['name', 'address', 'phone', 'email', 'comment']
        labels = {
            'name': "ПІБ",
            'address': "Адреса доставки",
            'phone': "Номер телефону",
            'email': "Електронна пошта",
            'comment': "Коментар до замовлення",
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }