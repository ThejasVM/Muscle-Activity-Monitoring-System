from django.urls import path
from . import views

urlpatterns = [
    path('live-graph/', views.live_graph, name='live_graph'),
]
