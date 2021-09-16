
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')),
    path('accounts/<int:username>/food/', include('food.urls')),
    path('exercise/', include('exercise.urls')),
    path('food/', include('fooddb.urls')),
]