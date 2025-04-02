from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Priority(models.Model):
    name = models.CharField(max_length=64)
    level = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "priorities"
        ordering = ['level']

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "statuses"
        ordering = ['order']

    def __str__(self):
        return self.name

class Issue(models.Model):
    title = models.CharField(max_length=128, default="Untitled Issue")
    summary = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reported_issues"
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="assigned_issues",
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('issues:detail', args=[str(self.id)])
