from django.urls import path

from .views import AboutPageView, HomePageView, PagePageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('page/', PagePageView.as_view(), name='page'),
]
