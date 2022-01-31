from django.urls import path
from tracker.views import TaskView, TaskCreateView, TaskDeleteView, ProjectDetailView, ProjectCreateView, \
    TaskEditView
from tracker.views import ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list_view'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail_view'),
    path('project/create', ProjectCreateView.as_view(), name='project_create_view'),
    path('task/details/<int:pk>', TaskView.as_view(), name='task_view'),
    path('project/<int:pk>/task/create', TaskCreateView.as_view(), name='task_create_view'),
    path('task/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete_view'),
    path('task/edit/<int:pk>', TaskEditView.as_view(), name='task_edit_view'),
]
