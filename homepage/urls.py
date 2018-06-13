from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
	path('', RedirectView.as_view(url='home/', permanent=False), name='redirect_home'),
	path('home/', views.HomePageView.as_view(), name='home'),
]
