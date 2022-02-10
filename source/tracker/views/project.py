from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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
        context = super().get_context_data(**kwargs)
        tasks = self.get_object().tasks.order_by('-date_created')
        print(tasks)
        context['tasks'] = tasks
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = 'project/project_create.html'

    def get_success_url(self):
        return reverse('project_detail_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_detail_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project_list_view')

