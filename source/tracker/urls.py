from django.urls import path
from tracker.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index_view")
]
