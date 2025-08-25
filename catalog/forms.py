from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field, forms.ModelMultipleChoiceField):
                field.widget.attrs['class'] = 'form-select multiple-select'
            else:
                field.widget.attrs['class'] = 'form-control'
            if field.required:
                field.error_messages = {
                    'required': 'Это поле обязательно для заполнения'
                }
            field.widget.attrs['placeholder'] = field.label


class ProductForm(StyleFormMixin, ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name', '').lower()
        return self._validate_forbidden_words(name, 'названии')

    def clean_description(self):
        description = self.cleaned_data.get('description', '').lower()
        return self._validate_forbidden_words(description, 'описании')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price

    def _validate_forbidden_words(self, text, field_name):
        """Проверяет текст на наличие запрещенных слов"""
        found_words = []

        for word in self.forbidden_words:
            if word in text:
                found_words.append(word)

        if found_words:
            raise forms.ValidationError(
                f"Обнаружены запрещенные слова в {field_name}: {', '.join(found_words)}"
            )

        if field_name == 'названии':
            return self.cleaned_data.get('name')
        else:
            return self.cleaned_data.get('description')
