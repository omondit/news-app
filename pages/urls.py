from pages.views import HomePageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
