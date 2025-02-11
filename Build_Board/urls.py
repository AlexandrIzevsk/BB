from django.urls import include, path
from .views import (
    AdvertList, OneAdvertDetail, AdvertCreate, AdvertUpdate
)


urlpatterns = [
    path('', AdvertList.as_view(), name='adverts'),
    path('<int:pk>', OneAdvertDetail.as_view(), name='advert_detail'),
    path('<int:pk>/update', AdvertUpdate.as_view(), name='advert_update'),
    path('create', AdvertCreate.as_view(), name='advert_edit'),
    path('__debug__/', include('debug_toolbar.urls'))
]