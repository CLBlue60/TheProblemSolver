from django import forms
from .models import Issue, Status

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'summary', 'description', 'assignee', 'status', 'priority']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['assignee'].queryset = user.team.customuser_set.all()

       
        if not self.instance.pk:
            try:
                self.fields['status'].initial = Status.objects.get(name="To-Do")
            except Status.DoesNotExist:
                self.fields['status'].initial = None

        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Brief issue title'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Short summary'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Detailed description'})
        self.fields['assignee'].widget.attrs.update({'class': 'form-select'})
