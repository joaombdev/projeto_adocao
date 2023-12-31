"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pets.views import NewPetCreateView, PetListView, PetDetailView, PetUptadeView, PetDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', PetListView.as_view(), name='pets_list'),
    path('new_pet/', NewPetCreateView.as_view(), name='new_pet'),
    path('car/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('car/<int:pk>/update/', PetUptadeView.as_view(), name='pet_update'),
    path('car/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
