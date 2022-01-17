from django.db import models

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')

    def __str__(self):
        return f'{self.pk}. {self.name}'

    class Meta:
        db_table = 'status'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Type(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')

    def __str__(self):
        return f'{self.pk}. {self.name}'

    class Meta:
        db_table = 'Type'
        verbose_name = 'Task'
        verbose_name_plural = 'Types'


class Task(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Summary')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    status = models.ForeignKey('tracker.Status', on_delete=models.PROTECT, related_name='tasks', verbose_name="Status")
    type = models.ManyToManyField('tracker.Type', related_name='tasks', verbose_name='Type')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Date updated")

    def __str__(self):
        return f'{self.pk}. {self.summary} {self.status}'

    class Meta:
        db_table = 'task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
