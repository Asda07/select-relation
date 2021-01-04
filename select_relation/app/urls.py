from django.urls import path
from . import views
urlpatterns=[
    path('s',views.select,name='select'),
    path('p',views.prefetch,name='prefetch'),
]