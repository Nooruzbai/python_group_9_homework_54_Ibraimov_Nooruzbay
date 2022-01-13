from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from tracker.forms import TaskForm
from tracker.models import Task

# Create your views here.


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks': tasks})


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        kwargs['task'] = task
        return super().get_context_data(**kwargs)


class CreateView(View):
    def get(self, request, *args, **kwargs ):
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get('summary')
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            type = form.cleaned_data.get('type')
            new_task = Task.objects.create(summary=summary, description=description, status=status, type=type)
            return redirect('index_view')
        return render(request, 'create_task.html', {'form': form})


class DeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'delete_task.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index_view')