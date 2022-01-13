from django.urls import path
from tracker.views import IndexView, TaskView

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('details/<int:pk>', TaskView.as_view(), name='task_view')
]
