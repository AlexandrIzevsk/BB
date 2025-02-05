from django.urls import include, path
from .views import (
    AdvertList, OneAdvertDetail,
)


urlpatterns = [
    path('', AdvertList.as_view()),
    path('adverts/<int:pk>', OneAdvertDetail.as_view(), name='advert_detail'),
    path('__debug__/', include('debug_toolbar.urls'))
]