from django.urls import path
from tracker.views import TaskIndexView, TaskView, TaskCreateView, TaskDeleteView, EditView, ProjectDetailView, ProjectCreateView
from tracker.views import ProjectListView



urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list_view'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail_view'),
    path('project/create', ProjectCreateView.as_view(), name='project_create_view'),
    path('tasks/', TaskIndexView.as_view(), name='task_index_view'),
    path('task/details/<int:pk>', TaskView.as_view(), name='task_view'),
    path('project/<int:pk>/task/create', TaskCreateView.as_view(), name='task_create_view'),
    path('task/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete_view'),
    # path('edit/<int:pk>', EditView.as_view(), name='edit_view'),

]

# urlpatterns = [
#     path('', IndexView.as_view(), name='index_view'),
#     path('details/<int:pk>', TaskView.as_view(), name='task_view'),
#     path('create/<int:pk>/task/create', TaskCreateView.as_view(), name='create_view'),
#     path('delete/<int:pk>', DeleteView.as_view(), name='delete_view'),
#     path('edit/<int:pk>', EditView.as_view(), name='edit_view'),
#     path('projects/', ProjectListView.as_view(), name='project_list_view'),
#     path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail_view'),
#     path('project/create', ProjectCreateView.as_view(), name='project_create_view')
# ]
