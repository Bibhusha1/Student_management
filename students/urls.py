from django.urls import path
from .import views

app_name = 'students'

urlpatterns = [
    path('',views.listing, name='listing'),
    path('add',views.add,name='add'),
    path('delete',views.delete,name='delete'),
    path('edit',views.edit,name='edit'),
]