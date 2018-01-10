from django import forms

class TodoForm(forms.Form):
	text = forms.CharField(max_length=30,
		widget=forms.TextInput(
			attrs={'placeholder': 'Enter todo'}))