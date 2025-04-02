from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Issue, Status, Priority
from .forms import IssueForm

class BoardView(ListView):
    template_name = "issues/board.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        statuses = Status.objects.all().order_by('order')

        status_lists = {}
        for status in statuses:
            status_lists[status] = Issue.objects.filter(status=status).order_by('-created_on')

        context['status_lists'] = status_lists
        return context

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issues:new_issue.html'
    success_url = reverse_lazy('issues:board')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['priorities'] = Priority.objects.all()
        return context


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issues/issue_form.html'
    success_url = reverse_lazy('issues:board')

    def get_queryset(self):
        return Issue.objects.filter(assignee__team=self.request.user.team)
