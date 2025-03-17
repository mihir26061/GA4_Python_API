from django.urls import path
from .views import GA4ServiceView

urlpatterns = [
    path('api/', GA4ServiceView.as_view(), name='ga4_service'),
]
