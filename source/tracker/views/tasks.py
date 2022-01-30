from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView
from django.db.models import Q
from tracker.forms import TaskForm, SearchForm
from tracker.models import Task

# Create your views here.


class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    paginate_by = 10
    paginate_orphans = 0
    context_object_name = "tasks"

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.order_by("date_created")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['form'] = SearchForm(initial={"search": self.search_value})
            context['search'] = self.search_value
        return context

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class TaskView(TemplateView):
    template_name = 'task/details.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        kwargs['task'] = task
        return super().get_context_data(**kwargs)


class CreateView(View):
    def get(self, request, *args, **kwargs ):
        form = TaskForm()
        return render(request, 'task/create.html', {'form': form})

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
        return render(request, 'task/create.html', {'form': form})


class DeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'task/delete.html', {'task': task})

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
        return render(request, 'task/edit.html', {'task': task, 'form': form})

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
        return render(request, 'task/edit.html', {'task': task, 'form': form})

