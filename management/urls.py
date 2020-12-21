from django.urls import path,include
from . import views

urlpatterns = [
    path('logOut',views.logout,name='logOut'),
    path('review',views.review,name='review'),
    path('delete_review',views.delete_review,name='delete_review'),
    path('query',views.query,name='query'),
    path('add_dest',views.add_dest,name='add_dest'),
    path('add_new_dest',views.add_new_dest,name='add_new_dest'),
    path('delete_data',views.delete_data,name='delete_data'),
    path('',views.management_index,name='management_index'),
]
