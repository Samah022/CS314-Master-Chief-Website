from . import views
from django.urls import path

urlpatterns = [

    path('Dinner',views.baby,name='Dinner'),
    path('Party',views.country,name='Party'),
    path('Wedding',views.product,name='Wedding'),


]
