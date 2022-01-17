from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from tracker.forms import TaskForm
from tracker.models import Task

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        tasks = Task.objects.all()
        print(tasks)
        kwargs['tasks'] = tasks
        return super().get_context_data(**kwargs)


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
            new_task = Task.objects.create(summary=summary, description=description, status=status)
            new_task.type.set(type)
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


class EditView(View):

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'type': task.type.all()
        })
        return render(request, 'edit_view.html', {'task': task, 'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if form.is_valid():
            task.summary = form.cleaned_data.get('summary')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.type.set(form.cleaned_data.get('type'))
            task.save()
            return redirect('index_view')
        return render(request, 'edit_view.html', {'task': task, 'form': form})

