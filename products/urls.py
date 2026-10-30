from django.urls import path
from.views import ProductAPIView, ProductListAPIView

urlpatterns = [
path("all/", ProductListAPIView.as_view()),
path("<slug:slug>/", ProductAPIView.as_view()),
]