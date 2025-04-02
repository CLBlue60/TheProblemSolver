from django.contrib import admin
from .models import Issue, Status, Priority

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'reporter', 'assignee', 'status', 'priority', 'created_on')
    list_filter = ('status', 'priority', 'created_on')
    search_fields = ('title', 'summary', 'description')
    raw_id_fields = ('reporter', 'assignee')
    date_hierarchy = 'created_on'
    ordering = ('-created_on',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'order')
    ordering = ('order',)

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    ordering = ('level',)
