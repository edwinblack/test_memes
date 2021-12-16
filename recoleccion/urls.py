from django.urls import path
# from . import views
from .views import HomePageView

urlpatterns = [
    # path('', views.async_view, name="home")
    path('', HomePageView.as_view(), name="home")
]