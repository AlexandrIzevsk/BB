from django import forms
from tinymce.widgets import TinyMCE
from .models import Advert, Feedback


class TinyMCEWidget(TinyMCE):
	def use_required_attribute(self, *args):
		return False


class PostForm(forms.ModelForm):
	content = forms.CharField(
		widget=TinyMCEWidget(
			attrs={'required': False, 'cols': 30, 'rows': 10}
		)
	)
	class Meta:
		model = Advert
		fields = [
            'choice',
            'title',
            'content',
        ]

class FeedbackForm(forms.ModelForm):

	class Meta:
		model = Feedback
		fields = [
			'advert',
			'text',
        ]


class FeedbackUpdateForm(forms.ModelForm):
	accept = True
	class Meta:
		model = Feedback
		fields = [
			'advert',
            'text',
			'accept',
        ]
