from django.contrib import admin
from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):
	class Meta:
		model = Menu
		fields = '__all__'
		widgets = {
			'fields': forms.Textarea(attrs={
				'rows': 10,
				'cols': 80,
				'placeholder': 'Введите поля меню в формате JSON'
			}),
		}

	def clean_fields(self):
		data = self.cleaned_data['fields']
		if not data.strip():
			raise forms.ValidationError("Это поле обязательно для заполнения")
		return data


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	form = MenuForm
	list_display = ('name', 'fields')
	list_display_links = ('name',)
	search_fields = ('name',)
	fieldsets = (
		('Основная информация', {
			'fields': ('name',),
			'description': 'Название меню должно быть уникальным'
		}),
		('Структура меню', {
			'fields': ('fields',),
			'classes': ('wide',),
			'description': 'Используйте JSON-формат'
		}),
	)
