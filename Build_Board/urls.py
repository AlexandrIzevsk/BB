from django.urls import include, path
from .views import (
    AdvertList, OneAdvertDetail, AdvertCreate, AdvertUpdate, feedback_confirm, feedback_delete
)


urlpatterns = [
    path('', AdvertList.as_view(), name='adverts'),
    path('feedback_confirm/<int:pk>/', feedback_confirm, name='feedback_confirm'),
    path('feedback_delete/<int:pk>/', feedback_delete, name='feedback_delete'),
    path('<int:pk>', OneAdvertDetail.as_view(), name='advert_detail'),
    path('<int:pk>/update', AdvertUpdate.as_view(), name='advert_update'),
    path('create', AdvertCreate.as_view(), name='advert_edit'),
    path('__debug__/', include('debug_toolbar.urls'))
]