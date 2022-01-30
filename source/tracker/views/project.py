from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.db.models import Q
from tracker.forms import ProjectForm
from tracker.models import Project


class ProjectListView(ListView):
    template_name = 'project/project_index.html'
    model = Project
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        tasks = self.get_object().tasks.order_by('-date_created')
        context['tasks'] = tasks
        return context


class ProjectCreateView(CreateView):
    form_class = ProjectForm
    template_name = 'project_creat.html'


