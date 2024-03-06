from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_visitor/<int:visitor_id>/', views.update_visitor, name='update_visitor'),
    path('delete_visitor/<int:visitor_id>', views.delete_visitor, name='delete_visitor')
]