from django.urls import path
from . import views
urlpatterns = [
    path('scrape-results' , views.scrape_results_type)
]
