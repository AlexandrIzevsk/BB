from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from .models import Feedback, Advert


class FeedbackFilter(FilterSet):

    def __init__(self, *args, **kwargs):
        super(FeedbackFilter, self).__init__(*args, **kwargs)
        self.filters['advert'].queryset = Advert.objects.filter(author=kwargs['request'])

    class Meta:
        model = Feedback
        fields = {
            'advert',
        }
