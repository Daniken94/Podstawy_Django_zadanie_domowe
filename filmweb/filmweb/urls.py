"""filmweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from filmweb_app.views import (AddMovie,
                               ModifyActor,
                               ModifyMovie,
                               MovieListView,
                               AddActor,
                               ActorListView,
                               DeleteMovieView,
                               DeleteActorView,
                               )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/new/', AddMovie.as_view(), name="add-movie"),
    path('', MovieListView.as_view(), name="movie-list"),
    path('actor/new/', AddActor.as_view(), name="add-actor"),
    path('actors/', ActorListView.as_view(), name="actor-list"),
    path('movie/delete/<int:id>/', DeleteMovieView.as_view(), name="delete-movie"),
    path('actor/delete/<int:id>/', DeleteActorView.as_view(), name="delete-actor"),
    path('movie/modify/<int:id>/', ModifyMovie.as_view(), name="modify-movie"),
    path('actor/modify/<int:id>/', ModifyActor.as_view(), name="modify-actor"),
]
