from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Issue, Status, Priority
from .forms import IssueForm

class BoardView(ListView):
    template_name = "issues/board.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['to_do_list'] = Issue.objects.filter(status__name__in=["To-Do", "Open"])
        context['in_progress_list'] = Issue.objects.filter(status__name="In-Progress")
        context['done_list'] = Issue.objects.filter(status__name="Done")
        context['statuses'] = Status.objects.all()  
        return context

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issues/new.html'
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
    template_name = 'issues/edit.html'
    success_url = reverse_lazy('issues:board')

class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = 'issues/delete.html'
    success_url = reverse_lazy('issues:board')

class ChangeStatusView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=pk)
        new_status_name = request.POST.get('status')

        try:
            new_status = Status.objects.get(name=new_status_name)
        except Status.DoesNotExist:
            return redirect('issues:board')


        if request.user != issue.reporter and not request.user.is_staff:
            return HttpResponseForbidden("You are not allowed to change the status of this issue.")


        issue.status = new_status
        issue.save()
        return redirect('issues:board')
