# YAASwebsite URL Configuration

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Domain/admin/
    path('admin/', admin.site.urls),
    # Domain/accounts/
    # path('account/', include('user_management.urls'), name='account'),
    # Domain/
    path('', include('home.urls'), name='home'),  # most be last
]
