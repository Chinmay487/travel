from django.urls import path
from . import views

urlpatterns = [
    path('ask',views.ask,name='ask'),
    path('submit_query',views.submit_query,name='submit_query'),
    path('About',views.about,name='about'),
    path('review',views.review,name='review'),
    path('feedback',views.feedback,name='feedback'),
    path('submit_feedback',views.submit_feedback,name='submit_feedback'),
    path('',views.index,name='index'),
]