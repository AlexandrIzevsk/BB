from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from .models import Advert


class FeedbackFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='advert__title',
        queryset=Advert.objects.all(),
        label='Advert',
        empty_label='Любая',
    )

    class Meta:
        model = Advert
        fields = {
            'title',
        }
