from django.shortcuts import render
from django.views.generic import View, TemplateView
from tracker.models import Task

# Create your views here.


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks': tasks})
