from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('pages.urls', 'pages'))),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('issues/', include(('issues.urls', 'issues'))),
]
