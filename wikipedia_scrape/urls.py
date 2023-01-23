from django.urls import path
from . import views
urlpatterns = [
    path("search" , views.function_Search , name = "search"),
    path("search-results" , views.scrape_results_Content_sub),
    # path('check_status' , views.check_status)
]
