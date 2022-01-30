from django.urls import path
from tracker.views.tasks import IndexView, TaskView, CreateView, DeleteView, EditView

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('details/<int:pk>', TaskView.as_view(), name='task_view'),
    path('create/', CreateView.as_view(), name='create_view'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete_view'),
    path('edit/<int:pk>', EditView.as_view(), name='edit_view')
]
