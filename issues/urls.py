from django.urls import path
from .views import BoardView, IssueCreateView, IssueUpdateView, IssueDeleteView, ChangeStatusView

app_name = 'issues'

urlpatterns = [
    path('board/', BoardView.as_view(), name='board'),
    path('create/', IssueCreateView.as_view(), name='create'),
    path('<int:pk>/update/', IssueUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='delete'),
    path('<int:pk>/change-status/', ChangeStatusView.as_view(), name='change_status'),  # New URL
]
