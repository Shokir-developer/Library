from django.urls import path
from .views import bookApi, bookAdd

urlpatterns = [
	path('', bookApi),
	path('add/', bookAdd)
]