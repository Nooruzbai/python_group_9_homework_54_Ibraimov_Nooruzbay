from django.urls import path
from tracker.views import IndexView, TaskView, CreateView, DeleteView, EditView, ProjectDetailView
from tracker.views import ProjectListView

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('details/<int:pk>', TaskView.as_view(), name='task_view'),
    path('create/', CreateView.as_view(), name='create_view'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete_view'),
    path('edit/<int:pk>', EditView.as_view(), name='edit_view'),
    path('projects/', ProjectListView.as_view(), name='project_list_view'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_list_view')
]
