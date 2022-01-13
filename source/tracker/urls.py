from django.urls import path
from tracker.views import IndexView, TaskView, CreateView, DeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('details/<int:pk>', TaskView.as_view(), name='task_view'),
    path('create/', CreateView.as_view(), name='create_view'),
    path('delee/', DeleteView.as_view(), name='delete_view')
]
