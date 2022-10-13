from django.urls import path
from . import views
from .views import IndexView

urlpatterns = [
    # path('', views.index, name="index"),
    path('', IndexView.as_view(), name="index"),
    # path('create/', views.create, name="create"),
    path('create/', views.PythonCreateView.as_view(), name="create"),
]
