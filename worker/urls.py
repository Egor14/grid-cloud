from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.log),
    path('sign/', views.sign),
    path('', views.index),
    path('logout/', views.out),
    path('add/', views.add)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
