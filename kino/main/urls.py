from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home
from .views import hall

urlpatterns = [
    path('', home, name='home'),
    path('hall<int:num>', hall)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)