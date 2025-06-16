from django.urls import path
from .views import ShortenURL, ExpandURL

urlpatterns = [
    path('shorten/', ShortenURL.as_view(), name='shorten_url'),
    path('shrt/<str:short_url>/', ExpandURL.as_view(), name='expand_url'),
]