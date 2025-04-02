from django.urls import path
from .views import BoardView, IssueCreateView, IssueUpdateView

app_name = 'issues'

urlpatterns = [
    path('board/', BoardView.as_view(), name='board'),
    path('create/', IssueCreateView.as_view(), name='create'),
    path('<int:pk>/update/', IssueUpdateView.as_view(), name='update'),
]
