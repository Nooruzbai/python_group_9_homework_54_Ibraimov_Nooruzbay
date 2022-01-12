from django.urls import path
from tracker.views import index_view

urlpatterns = [
    path('', index_view, name="index_view")
]
